import requests

token_goerli_address = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/tokenContract").json()['addresses']['goerli']

token_local_address = ""

token_abi = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/tokenContract").json()['abi']

token_bytecode = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/tokenContract").json()['bytecode']

ttBank_goerli_address = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/ttBank").json()['addresses']['goerli']

ttBank_local_address = ""

ttBank_abi = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/ttBank").json()['abi']

ttBank_bytecode = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/ttBank").json()['bytecode']


def token_addresses(network_id: int):

    if network_id == 5:
        return token_goerli_address

    if network_id == 1337:
        return token_local_address


def ttBank_addresses(network_id: int):

    if network_id == 5:
        return ttBank_goerli_address

    if network_id == 1337:
        return ttBank_local_address
