from web3 import Web3

from src.network import *


class Token:
    def __init__(self, network_id, provider_url):
        self.network_id = network_id

        self.provider = provider_url

        self.w3 = Web3(Web3.HTTPProvider(provider_url))

        self.contract = self.w3.eth.contract(
            address=token_addresses(network_id), abi=token_abi)

    def fetch_address(self):
        return self.contract.address

    def fetch_name(self):
        return self.contract.functions.name().call()
