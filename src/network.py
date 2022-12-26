
from src.contractApi import *

from src.local_addresses import *


def token_addresses(network_id: int):
    """ Returns the Token.sol address associated with the network_id

    Args:
        network_id (int): _description_

    Returns:
        _type_: _description_
    """
    if network_id == 5:
        return token_goerli_address

    if network_id == 1337:

        return addresses["token_local_address"]


def ttBank_addresses(network_id: int):

    if network_id == 5:
        return ttBank_goerli_address

    if network_id == 1337:

        return addresses["ttBank_local_address"]
