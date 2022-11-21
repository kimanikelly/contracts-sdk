
from src.contractApi import *

from src.deploy import deploy_contracts


# def token_addresses(network_id: int):

#     if network_id == 5:
#         return token_goerli_address

#     if network_id == 1337:
#         return deploy_contracts['token'].address


def contract_addresses(network_id: int):

    if network_id == 5:

        return ttBank_goerli_address

    if network_id == 1337:

        return {
            "token": deploy_contracts()['ttBank'].address,
            "ttBank": deploy_contracts()['ttBank'].address
        }
