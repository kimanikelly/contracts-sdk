from src.ttBank import *
from src.token import *

from src.deploy import *
from src.local_addresses import *
import pytest


@pytest.fixture
def token():

    addresses["token_local_address"] = deploy_token().address

    return Token(1337, "http://localhost:8545")


@pytest.fixture
def ttBank():

    addresses["ttBank_local_address"] = deploy_ttBank().address

    return TTBank(1337, "http://localhost:8545")
