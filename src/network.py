
from src.contract_api import *

from src.local_addresses import *


def token_addresses(network_id: int) -> str:
    """ Returns the Token.sol address associated with the network_id

    Args:
        network_id (int): The numeric value used to connect with Ethereum compatible protocols

    Returns:
        str: The Token.sol address
    """

    # Checks if the network routes to Goerli testnet
    if network_id == 5:
        return token_goerli_address

    # Checks if the network routes to Ganache locally
    if network_id == 1337:
        return addresses["token_local_address"]


def ttBank_addresses(network_id: int) -> str:
    """ Returns the TTBank.sol address associated with the network_id

    Args:
        network_id (int): The numeric value used to connect with Ethereum compatible protocols

    Returns:
        str: The TTBank.sol address
    """

    # Checks if the network routes to Goerli testnet
    if network_id == 5:
        return ttBank_goerli_address

    # Checks if the network routes to Ganache locally
    if network_id == 1337:

        return addresses["ttBank_local_address"]
