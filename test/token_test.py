from src.token import *

import pytest


@pytest.fixture
def token():
    return Token(1337, "http://localhost:8545")


def test_fetch_name(token):

    assert (token.fetch_name() == "TEST TOKEN")
