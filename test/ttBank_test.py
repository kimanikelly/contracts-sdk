from src.ttBank import *

from src.token import *

from src.deploy import *

import pytest


@pytest.fixture
def contract():
    return (TTBank(1337, "http://localhost:8545"), Token(1337, "http://localhost:8545"))


def test_open_account(contract):

    print(contract[0].fetch_token_address())
    print(contract[1].fetch_address())
