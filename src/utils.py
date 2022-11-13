import requests

ttBank_goerli_address = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/ttBank").json()['addresses']['goerli']

ttBank_abi = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/ttBank").json()['abi']


def ttBank_addresses(networkId: int):

    if networkId == 5:
        return ttBank_goerli_address
