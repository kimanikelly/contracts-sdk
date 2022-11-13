from src.network import *

from web3 import Web3

provider = w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

w3.eth.default_account = w3.eth.accounts[0]


def deploy_token():

    Token = w3.eth.contract(abi=token_abi, bytecode=token_bytecode)

    tx_hash = Token.constructor().transact()

    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    token = w3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=token_abi
    )

    token.functions.initialize("TEST TOKEN", "TT").transact()

    return token


def deploy_ttBank():

    TTBank = w3.eth.contract(abi=ttBank_abi, bytecode=ttBank_bytecode)

    tx_hash = TTBank.constructor().transact()

    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    ttBank = w3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=ttBank_abi
    )

    ttBank.functions.initialize(deploy_token().address).transact()

    return ttBank
