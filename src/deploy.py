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


def deploy_contracts():

    Token = w3.eth.contract(abi=token_abi, bytecode=token_bytecode)

    token_tx_hash = Token.constructor().transact()

    token_tx_receipt = w3.eth.wait_for_transaction_receipt(token_tx_hash)

    token = w3.eth.contract(
        address=token_tx_receipt.contractAddress,
        abi=token_abi
    )

    token.functions.initialize("TEST TOKEN", "TT").transact()

    TTBank = w3.eth.contract(abi=ttBank_abi, bytecode=ttBank_bytecode)

    ttBank_tx_hash = TTBank.constructor().transact()

    ttBank_tx_receipt = w3.eth.wait_for_transaction_receipt(ttBank_tx_hash)

    ttBank = w3.eth.contract(
        address=ttBank_tx_receipt.contractAddress,
        abi=ttBank_abi
    )

    ttBank.functions.initialize(token.address).transact()

    print("TTBANK IN DEPLOY", ttBank.address)
    return {
        "token": token,
        "ttBank": ttBank
    }
