from web3 import Web3

from src.ttBank import *

from dotenv import load_dotenv

import os

load_dotenv()


def test_ttBank_instance():

    ttBank = TTBank(5, os.getenv("PROVIDER_URL"))
