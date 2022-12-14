from src.ttBank import *
from src.token import *

from src.deploy import *
from src.local_addresses import *
import pytest


@pytest.fixture
def account0():
    return w3.eth.accounts[0]


@pytest.fixture
def account1():
    return w3.eth.accounts[1]


@pytest.fixture
def token():

    addresses["token_local_address"] = deploy_token().address

    return Token(1337, "http://localhost:8545")


@pytest.fixture
def ttBank():

    addresses["ttBank_local_address"] = deploy_ttBank().address

    return TTBank(1337, "http://localhost:8545")


def test_ttbank_instance(ttBank, account0):

    # Verify fetch_owner() returns the address of the account[0]
    assert (ttBank.fetch_owner() == account0)
