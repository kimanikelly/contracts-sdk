from web3 import Web3

from src.network import *


class TTBank:
    def __init__(self, account, network_id, provider_url):

        # Connected Wallet
        self.account = account

        self.network_id = network_id

        self.provider = provider_url

        self.w3 = Web3(Web3.HTTPProvider(provider_url))

        self.contract = self.w3.eth.contract(
            address=ttBank_addresses(network_id), abi=ttBank_abi)

        self.address = self.contract.address

    def fetch_owner(self):
        """
        Returns TTBank.sol owner address
        """
        return self.contract.functions.owner().call()

    def fetch_token_address(self):
        """
        Returns the Token.sol contracta address
        """
        return self.contract.functions.token().call()

    def fetch_account(self):
        """
        Returns the account details
        """
        return self.contract.functions.viewAccount().call()

    def fetch_balance(self):
        return self.contract.functions.viewBalance().call()

    def fetch_bank_balance(self):
        return self.contract.functions.bankBalance().call()

    def open_account(self, starting_balance: int):
        return self.contract.functions.openAccount(self.w3.toWei(starting_balance, "ether")).transact({"from": self.account})

    def deposit(self, amount):
        return self.contract.functions.deposit(self.w3.toWei(amount, "ether")).transact({"from": self.account})

    def withdraw(self, amount):
        return self.contract.functions.withdraw(self.w3.toWei(amount, "ether")).transact({"from": self.account})
