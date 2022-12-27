from web3 import Web3

from src.network import *


class TTBank:

    def __init__(self, account: str, network_id: int, provider_url: str):
        """ Creates the off-chain abstraction of the TTBank.sol Smart Contract and its functionalities as a Class

        Args:
            account (str): The Ethereum wallet used to connect and instantiate the TTBank class

            network_id (int): The numeric value used to connect with Ethereum compatible protocols

            provider_url( str): The abstraction of a connection to the Ethereum network

        """

        # account is set as a TTBank class property
        self.account = account

        # network_id is set as a TTBank class property
        self.network_id = network_id

        # provider is set as a TTBank class property
        self.provider = provider_url

        # w3 is set as a TTBank class property. Utilizes the Web3.py library for interacting with Ethereum
        self.w3 = Web3(Web3.HTTPProvider(provider_url))

        # contract is set as a TTBank class property. Instantiates the TTBank.sol Smart Contract
        self.contract = self.w3.eth.contract(
            address=ttBank_addresses(network_id), abi=ttBank_abi)

        # address is set as a TTBank class property. Returns the TTBank Smart Contract address
        self.address = self.contract.address

    def fetch_owner(self):
        """Returns TTBank.sol owner address

         Returns:
             str: The owners Ethereum wallet address
         """
        return self.contract.functions.owner().call()

    def fetch_token_address(self):
        """Returns the Token.sol contract address

        Returns:
            str: Contract address of Token.sol
        """
        return self.contract.functions.token().call()

    def fetch_account(self):
        """Returns the accounts details

        """
        return self.contract.functions.viewAccount().call()

    def fetch_balance(self):
        """Returns the accounts Test Token balance
        Returns:
            int: The Test Token amount
        """
        return self.contract.functions.viewBalance().call()

    def fetch_bank_balance(self):
        """Returns the Test Token balance within TTBank.sol

        Returns:
            int: The Test Token amount
        """
        return self.contract.functions.bankBalance().call()

    def open_account(self, starting_balance: int):
        """Allows the account to open an account with TTBank and make an initial deposit

        Args:
            amount (int): The amount of Test Tokens the account wants to deposit into their account balance

        """
        return self.contract.functions.openAccount(self.w3.toWei(starting_balance, "ether")).transact({"from": self.account})

    def deposit(self, amount: int):
        """Allows the account to deposit TestTokens into their existing account balance

        Args:
            amount (int): The amount of Test Tokens the account wants to deposit into their account balance

        """
        return self.contract.functions.deposit(self.w3.toWei(amount, "ether")).transact({"from": self.account})

    def withdraw(self, amount: int):
        """Allows the signer to withdraw a specified amount Test Tokens from their bank account

        Args:
            amount (int): The amount of Test Tokens to withdraw from the account

        """
        return self.contract.functions.withdraw(self.w3.toWei(amount, "ether")).transact({"from": self.account})
