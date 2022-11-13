import requests

token_goerli_address = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/tokenContract").json()['addresses']['goerli']

token_abi = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/tokenContract").json()['abi']

token_bytecode = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/tokenContract").json()['bytecode']

ttBank_goerli_address = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/ttBank").json()['addresses']['goerli']

ttBank_abi = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/ttBank").json()['abi']

ttBank_bytecode = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/ttBank").json()['bytecode']
