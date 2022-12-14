from web3 import Web3

from src.network import *


class TTBank:
    def __init__(self, network_id, provider_url):
        self.network_id = network_id

        self.provider = provider_url

        self.w3 = Web3(Web3.HTTPProvider(provider_url))

        self.contract = self.w3.eth.contract(
            address=ttBank_addresses(network_id), abi=ttBank_abi)

        self.address = self.contract.address

    def fetch_owner(self):
        return self.contract.functions.owner().call()

    def fetch_token_address(self):
        return self.contract.functions.token().call()

    def fetch_account(self):
        return self.contract.functions.viewAccount().call()

    def open_account(self, startingBalance: int):
        return self.contract.functions.openAccount(startingBalance).transact()
