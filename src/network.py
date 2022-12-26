
from src.contractApi import *

from src.local_addresses import *


def token_addresses(network_id: int):

    if network_id == 5:
        return token_goerli_address

    if network_id == 1337:

        return addresses["token_local_address"]


def ttBank_addresses(network_id: int):

    if network_id == 5:
        return ttBank_goerli_address

    if network_id == 1337:

        return addresses["ttBank_local_address"]
