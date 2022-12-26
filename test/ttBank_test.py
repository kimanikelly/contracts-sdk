from src.ttBank import *
from src.token_erc20 import *

from src.deploy import *
from src.local_addresses import *
import pytest


mint_amount = 200
fund_amount = 100
starting_balance = 50

addresses["token_local_address"] = deploy_token().address
addresses["ttBank_local_address"] = deploy_ttBank().address


@pytest.fixture
def account0():
    return w3.eth.accounts[0]


@pytest.fixture
def account1():
    return w3.eth.accounts[1]


@pytest.fixture
def token(account0):
    return Token(account0, 1337, "http://localhost:8545")


@pytest.fixture
def ttBank(account0):
    return TTBank(account0, 1337, "http://localhost:8545")
