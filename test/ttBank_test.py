from web3 import Web3

from src.ttBank import *

from src.deploy import *

from dotenv import load_dotenv

import os

import pytest

load_dotenv()


@pytest.fixture
def deploy():
    return deploy_token(), deploy_ttBank()
