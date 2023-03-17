import requests

token_goerli_address = requests.get(
    "https://smart-contracts-api-node.herokuapp.com/token").json()['addresses']['goerli']

token_abi = requests.get(
    "https://smart-contracts-api-node.herokuapp.com/token").json()['abi']

token_bytecode = requests.get(
    "https://smart-contracts-api-node.herokuapp.com/token").json()['bytecode']

ttBank_goerli_address = requests.get(
    "https://smart-contracts-api-node.herokuapp.com/ttBank").json()['addresses']['goerli']

ttBank_abi = requests.get(
    "https://smart-contracts-api-node.herokuapp.com/ttBank").json()['abi']

ttBank_bytecode = requests.get(
    "https://smart-contracts-api-node.herokuapp.com/ttBank").json()['bytecode']
