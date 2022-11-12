import requests

ttBank_rinkeby_address = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/ttBank").json()['addresses']['rinkeby']

ttBank_abi = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/ttBank").json()['abi']


def ttBank_addresses(networkId: int):

    if networkId == 42:
        return ttBank_rinkeby_address
