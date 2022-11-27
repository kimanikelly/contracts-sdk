from src.token import *

from src.deploy import *
from src.local_addresses import *
import pytest

mintAmount = 100


@pytest.fixture
def account0():
    return w3.eth.accounts[0]


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

    # Verify mint() is able mint ERC-20 tokens only by the owner
    token.mint(mintAmount)

    # Verify fetch_total_supply returns and increases by the mint amount
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
