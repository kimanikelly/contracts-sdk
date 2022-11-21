
from src.contractApi import *

from src.deploy import deploy_contracts
from src.deploy import deploy_token


def token_addresses(network_id: int):

    if network_id == 5:
        return token_goerli_address

    if network_id == 1337:
        return deploy_token().address


def contract_addresses(network_id: int):

    if network_id == 5:

        return ttBank_goerli_address

    if network_id == 1337:

        return {
            "token": deploy_contracts()['ttBank'].address,
            "ttBank": deploy_contracts()['ttBank'].address
        }
