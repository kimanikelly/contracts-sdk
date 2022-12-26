from web3 import Web3

from src.network import *


class Token:
    def __init__(self, account: str, network_id: int, provider_url: str):
        """ Creates the off-chain abstraction of the Token.sol Smart Contract and its functionalities as a Class

        Args:
            account (str): The Ethereum wallet used to connect and instantiate the Token class

            network_id (int): The numeric value used to connect with Ethereum compatible protocols

            provider_url( str): The abstraction of a connection to the Ethereum network

        """

        # account is set as a Token class property
        self.account = account

        # network_id is set as a Token class property
        self.network_id = network_id

        # provider is set as a Token class property
        self.provider = provider_url

        # w3 is set as a Token class property. Utilizes the Web3.py library for interacting with Ethereum
        self.w3 = Web3(Web3.HTTPProvider(provider_url))

        # contract is set as a Token class property. Instantiates the Token Smart Contract
        self.contract = self.w3.eth.contract(
            address=token_addresses(network_id), abi=token_abi)

        # address is set as a TTBank class property. Returns the Token Smart Contract address
        self.address = self.contract.address

    def fetch_owner(self):
        """Returns Token.sol owner address

         Returns:
             str: The owners Ethereum wallet address
        """
        return self.contract.functions.owner().call()

    def fetch_name(self):
        """Returns the Token.sol name

        Returns:
            str: ERC-20 name of Token.sol
        """
        return self.contract.functions.name().call()

    def fetch_symbol(self):
        """Returns the Token.sol symbol

        Returns:
            str: ERC-20 symbol of Token.sol
        """
        return self.contract.functions.symbol().call()

    def fetch_decimals(self):
        """Returns the Token.sol contract decimals

        Returns:
            int: ERC-20 decimals of Token.sol
        """
        return self.contract.functions.decimals().call()

    def fetch_total_supply(self):
        """Returns the Token.sol contract total supply of minted tokens

        Returns:
            int: Total minted ERC-20 tokens
        """

        return self.contract.functions.totalSupply().call()

    def fetch_balance_of(self, address: str):
        """Returns the Test Token balance of an Ethereum address

        Returns:
            int: Test Token ERC-20 balance
        """
        return self.contract.functions.balanceOf(address).call()

    def fetch_fund_amount(self):
        """ The amount of ERC-20 tokens transferred to the account on `fund_account`
        """
        return self.contract.functions.fundAmount().call()

    def mint(self, amount: int):
        """ Creates and allocates ERC-20 tokens to Token.sol. This function
            can only be invoked by the owner.

            Args:
            amount (int): The amount of ERC-20 token the owner can allocate
        """
        return self.contract.functions.mint(amount).transact({"from":  self.account})

    def set_fund_amount(self, amount: int):
        """ Sets the amount of ERC-20 tokens that can be transferred to the account. This function can only
            be invoked by the owner.

            Args:
            amount (int): The amount of ERC-20 token the owner set
        """
        return self.contract.functions.setFundAmount(amount).transact({"from": self.account})

    def fund_account(self):
        """ Funds the msg.sender the fund amount.

        """
        return self.contract.functions.fundAccount().transact({"from": self.account})

    def transfer(self, to: str, amount: int):
        return self.contract.functions.transfer(to, self.w3.toWei(amount, "ether")).transact({"from": self.account})

    def allowance(self, owner: str, spender: str):
        return self.contract.functions.allowance(owner, spender).call()

    def approve(self, spender: str, amount: int):
        return self.contract.functions.approve(spender, self.w3.toWei(amount, "ether")).transact({"from": self.account})
