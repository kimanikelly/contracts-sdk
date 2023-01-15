from src.token_erc20 import *

from test.deploy import *
from src.local_addresses import *
import pytest

mintAmount = 100
fundAmount = 100

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


def test_token_instance(token, account0):

    # Verify fetch_owner() returns the address of the account[0]
    assert (token.fetch_owner() == account0)

    # Verify fetch_name() returns the ERC-20 name set at deployment
    assert (token.fetch_name() == "TEST TOKEN")

    # Verify fetch_symbol() returns the ERC-20 symbol set at deployment
    assert (token.fetch_symbol() == "TT")

    # Verify fetch_decimals returns ERC-20 decimals
    assert (token.fetch_decimals() == 18)


def test_total_supply(token):

    # Verify the total supply is 0 at initial deployment pre mint
    pre_mint_supply = token.fetch_total_supply()
    assert (pre_mint_supply == 0)

    signed_tx = w3.eth.account.sign_transaction(
        token.mint(mintAmount), private_key=account0_private_key)

    w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # Verify fetch_total_supply returns and increases by the mint amount
    post_mint_supply = token.fetch_total_supply()
    assert (post_mint_supply == w3.toWei(100, "ether"))


def test_balance_of(token):

    # Verify fetch_balance_of() returns a zero token balance pre mint
    pre_mint_balance = token.fetch_balance_of(token.address)
    assert (pre_mint_balance == 0)

    signed_tx = w3.eth.account.sign_transaction(
        token.mint(mintAmount), private_key=account0_private_key)

    w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # Verify fetch_balance_of() returns the Token.sol ERC-20 balance post mint
    post_mint_balance = token.fetch_balance_of(token.address)
    assert (post_mint_balance == w3.toWei(100, "ether"))


def test_mint(token):
    signed_tx = w3.eth.account.sign_transaction(
        token.mint(mintAmount), private_key=account0_private_key)

    w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    post_mint_balance = token.fetch_balance_of(token.address)
    assert (post_mint_balance == w3.toWei(100, "ether"))

    post_mint_supply = token.fetch_total_supply()
    assert (post_mint_supply == w3.toWei(100, "ether"))


def test_fund_amount(token):

    signed_tx = w3.eth.account.sign_transaction(
        token.mint(mintAmount), private_key=account0_private_key)

    w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # Verify fetch_fund_amount returns 0 before the owner sets the amount
    assert(token.fetch_fund_amount() == 0)

    # Verify set_fund_amounts sets the amount of TEST TOKENS an account receives
    token.set_fund_amount(fundAmount)

    # Verify fetch_fund_amount returns the fundAmount after the owner sets the amount
    assert(token.fetch_fund_amount() == w3.toWei(100, "ether"))


def test_fund_account(token, account0):

    # Token.sol balance should be 0 pre mint
    token_pre_mint_balance = token.fetch_balance_of(token.address)
    assert(token_pre_mint_balance == 0)

    signed_tx = w3.eth.account.sign_transaction(
        token.mint(mintAmount), private_key=account0_private_key)

    w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # Token.sol balance should be the mint amount post mint
    token_post_mint_balance = token.fetch_balance_of(token.address)
    assert(token_post_mint_balance == w3.toWei(100, "ether"))

    # Account0 should have a balance of 0 pre funding
    account0_pre_fund_balance = token.fetch_balance_of(account0)
    assert(account0_pre_fund_balance == 0)

    pre_fund_amount = token.fetch_fund_amount()
    assert(pre_fund_amount == 0)

    # Verify set_fund_amounts sets the amount of TEST TOKENS an account receives
    token.set_fund_amount(fundAmount)

    post_fund_amount = token.fetch_fund_amount()
    assert(post_fund_amount == w3.toWei(100, "ether"))

    # Account0 will be funded 100 TEST TOKENS from Token.sol
    token.fund_account()

    # Token.sol balance should decrease by the post_fund_amount
    token_post_fund_balance = token.fetch_balance_of(token.address)
    assert(token_post_fund_balance == token_post_mint_balance - post_fund_amount)

    # Account0 balance should increase by the fundAmount
    account0_post_fund_balance = token.fetch_balance_of(account0)
    assert(account0_post_fund_balance ==
           account0_pre_fund_balance + post_fund_amount)


def test_transfer(token, account0, account1):
    signed_tx = w3.eth.account.sign_transaction(
        token.mint(mintAmount), private_key=account0_private_key)

    w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # Verify set_fund_amounts sets the amount of TEST TOKENS an account receives
    token.set_fund_amount(fundAmount)

    # Account0 will be funded 100 TEST TOKENS from Token.sol
    token.fund_account()

    account0_pre_balance = token.fetch_balance_of(account0)

    account1_pre_balance = token.fetch_balance_of(account1)
    assert(account1_pre_balance == 0)

    token.transfer(account1, 10)

    account0_post_bal = token.fetch_balance_of(account0)
    assert(account0_post_bal == account0_pre_balance - w3.toWei(10, "ether"))

    account1_post_bal = token.fetch_balance_of(account1)
    assert(account1_post_bal == w3.toWei(10, "ether"))


def test_approval_allowance(token, account0, account1):

    token.approve(account1, 100)

    account0_allowance = token.allowance(account0, account1)

    assert (account0_allowance == w3.toWei(100, "ether"))
