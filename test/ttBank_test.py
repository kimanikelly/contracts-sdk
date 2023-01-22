from src.ttBank import *
from src.token_erc20 import *

from test.deploy import *
from src.local_addresses import *
import pytest


mint_amount = 200
fund_amount = 100
starting_balance = 50


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
def ttBank(account0):

    addresses["ttBank_local_address"] = deploy_ttBank().address

    return TTBank(account0, 1337, "http://localhost:8545")


def test_ttBank_instance(ttBank, account0):
    assert(ttBank.account == account0)

    assert(ttBank.network_id == 1337)

    assert(ttBank.provider == "http://localhost:8545")

    assert(ttBank.contract.address == ttBank.address)

    assert(ttBank.fetch_owner() == account0)
