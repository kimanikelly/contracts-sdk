from web3 import Web3

from src.utils import *


class TTBank:
    def __init__(self, network_id, provider_url):
        self.network_id = network_id

        self.provider = provider_url

        self.w3 = Web3(Web3.HTTPProvider(provider_url))

        self.contract = self.w3.eth.contract(
            address=ttBank_addresses(network_id), abi=ttBank_abi)

    def fetchToken(self):
        return self.contract.functions.token().call()

    def fetchAccount(self):
        return self.contract.functions.viewAccount().call()
