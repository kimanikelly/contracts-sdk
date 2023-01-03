from src.network import *

from web3 import Web3

from src.local_addresses import *

provider = w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

w3.eth.default_account = w3.eth.accounts[0]


def deploy_token():

    # Token.sol base class
    Token = w3.eth.contract(abi=token_abi, bytecode=token_bytecode)

    # Token.sol deployment
    tx_hash = Token.constructor().transact({
        "from": w3.eth.default_account})

    # Token.sol deployment receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    # Token.sol contract instance
    token = w3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=token_abi
    )

    # Token.sol initialization
    token.functions.initialize("TEST TOKEN", "TT").transact({
        "from": w3.eth.default_account})

    return token


def deploy_ttBank():

    TTBank = w3.eth.contract(abi=ttBank_abi, bytecode=ttBank_bytecode)

    ttBank_tx_hash = TTBank.constructor().transact({
        "from": w3.eth.default_account})

    ttBank_tx_receipt = w3.eth.wait_for_transaction_receipt(ttBank_tx_hash)

    ttBank = w3.eth.contract(
        address=ttBank_tx_receipt.contractAddress,
        abi=ttBank_abi
    )
    ttBank.functions.initialize(addresses["token_local_address"]).transact({
        "from": w3.eth.default_account})

    return ttBank
