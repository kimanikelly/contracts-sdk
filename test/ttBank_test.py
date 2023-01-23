from src.ttBank import *
from src.token_erc20 import *

from test.deploy import *
from src.local_addresses import *
import pytest


mint_amount = 200

fund_amount = 100

starting_balance = 50

account0_private_key = "0x76dc59c3f2cf8245cd3c191f0c40c72545bf361b8dd660276658e0e051294e45"


@pytest.fixture
def account0():
    return w3.eth.accounts[0]


@pytest.fixture
def account1():
    return w3.eth.accounts[1]


@pytest.fixture
def token(account0):

    addresses["token_local_address"] = deploy_token().address

    return Token(account0, 1337, "http://localhost:8545")


@pytest.fixture
def ttBank(account0, token):

    addresses["token_local_address"] = token.address
    addresses["ttBank_local_address"] = deploy_ttBank().address

    return TTBank(account0, 1337, "http://localhost:8545")


def test_ttBank_instance(ttBank, token, account0):
    assert(ttBank.account == account0)

    assert(ttBank.network_id == 1337)

    assert(ttBank.provider == "http://localhost:8545")

    assert(ttBank.contract.address == ttBank.address)

    assert(ttBank.fetch_owner() == account0)

    assert(ttBank.fetch_token_address() == token.address)


def test_open_account(ttBank, token, account0):
    mint_amount = 100

    fund_amount = 100

    signed_mint_tx = w3.eth.account.sign_transaction(
        token.mint(mint_amount), private_key=account0_private_key)

    w3.eth.send_raw_transaction(signed_mint_tx.rawTransaction)

    set_fund_amount_tx = w3.eth.account.sign_transaction(
        token.set_fund_amount(fund_amount), private_key=account0_private_key)

    w3.eth.send_raw_transaction(set_fund_amount_tx.rawTransaction)

    signed_fund_account_tx = w3.eth.account.sign_transaction(
        token.fund_account(), private_key=account0_private_key)

    w3.eth.send_raw_transaction(signed_fund_account_tx.rawTransaction)

    signed_approve_tx = w3.eth.account.sign_transaction(
        token.approve(ttBank.address, starting_balance), private_key=account0_private_key)

    w3.eth.send_raw_transaction(signed_approve_tx.rawTransaction)

    signed_open_account_tx = w3.eth.account.sign_transaction(
        ttBank.open_account(starting_balance), private_key=account0_private_key)

    w3.eth.send_raw_transaction(signed_open_account_tx.rawTransaction)

    on_chain_acct = ttBank.fetch_account()

    assert(on_chain_acct[0] == 1)

    assert(on_chain_acct[1] == account0)

    assert(on_chain_acct[2] == w3.toWei(starting_balance, "ether"))

    on_chain_acct_balance = ttBank.fetch_account_balance()

    assert(on_chain_acct_balance == w3.toWei(starting_balance, "ether"))
