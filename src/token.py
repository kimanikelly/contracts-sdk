from web3 import Web3

from src.network import *


class Token:
    def __init__(self, account, network_id, provider_url,):

        # Connected Wallet
        self.account = account

        self.network_id = network_id

        self.provider = provider_url

        self.w3 = Web3(Web3.HTTPProvider(provider_url))

        self.contract = self.w3.eth.contract(
            address=token_addresses(network_id), abi=token_abi)

        self.address = self.contract.address

    def fetch_owner(self):
        return self.contract.functions.owner().call()

    def fetch_name(self):
        return self.contract.functions.name().call()

    def fetch_symbol(self):
        return self.contract.functions.symbol().call()

    def fetch_decimals(self):
        return self.contract.functions.decimals().call()

    def fetch_total_supply(self):
        return self.contract.functions.totalSupply().call()

    def fetch_balance_of(self, address):
        return self.contract.functions.balanceOf(address).call()

    def mint(self, amount):
        return self.contract.functions.mint(amount).transact({"from":  self.account})

    def transfer(self, to, amount):
        return self.contract.functions.transfer(to, amount).transact({"from": self.account})
