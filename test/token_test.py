from src.token import *

from src.deploy import *
from src.local_addresses import *
import pytest

mintAmount = 100


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


def test_total_supply(token):

    pre_mint_supply = token.fetch_total_supply()
    assert (pre_mint_supply == 0)

    # 100 TEST TOKENS minted
    token.mint(mintAmount)

    post_mint_supply = token.fetch_total_supply()
    assert (post_mint_supply == 100e18)


def test_balance_of(token):

    pre_mint_balance = token.fetch_balance_of(token.address)
    assert (pre_mint_balance == 0)

    # 100 TEST TOKENS minted
    token.mint(mintAmount)

    post_mint_balance = token.fetch_balance_of(token.address)
    assert (post_mint_balance == 100e18)


def test_mint(token):
    # 100 TEST TOKENS minted
    token.mint(mintAmount)

    post_mint_balance = token.fetch_balance_of(token.address)
    assert (post_mint_balance == 100e18)

    post_mint_supply = token.fetch_total_supply()
    assert (post_mint_supply == 100e18)
