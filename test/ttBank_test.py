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


def test_open_account(token, ttBank, account0):

    print(token.address)

    # print(token.address)

    # print(token(account0).address)
    # print(token(account0).address)

    # token(account0).mint(mint_amount)

    # token(account0).set_fund_amount(fund_amount)

    # token(account0).fund_account()

    # token(account0).approve(token(account0).address, starting_balance)

    # ttBank(account0).open_account(starting_balance)
