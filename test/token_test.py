from src.token import *

from src.deploy import *
from src.local_addresses import *
import pytest


@pytest.fixture
def account1():
    return w3.eth.accounts[0]


@pytest.fixture
def token(account1):

    addresses["token_local_address"] = deploy_token().address

    return Token(account1, 1337, "http://localhost:8545")


def test_token_instance(token, account1):
    assert (token.fetch_owner() == account1)
    assert (token.fetch_name() == "TEST TOKEN")
    assert (token.fetch_symbol() == "TT")
    assert (token.fetch_decimals() == 18)


def test_total_supply(token, account1):

    # Verfiy the total TEST TOKEN supply is 0 before minting
    initial_total_supply = token.fetch_total_supply()
    assert (initial_total_supply == 0)

    token.mint(10)

    print(token.fetch_balance_of(token.address))
