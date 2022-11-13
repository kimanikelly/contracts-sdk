
from src.contractApi import *

from src.deploy import deploy_token, deploy_ttBank


def token_addresses(network_id: int):

    if network_id == 5:
        return token_goerli_address

    if network_id == 1337:
        return deploy_token().address


def ttBank_addresses(network_id: int):

    if network_id == 5:
        return ttBank_goerli_address

    if network_id == 1337:

        return deploy_ttBank().address
