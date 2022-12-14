import requests

token_goerli_address = requests.get(
    "http://ec2-34-203-42-249.compute-1.amazonaws.com/token").json()['addresses']['goerli']

token_abi = requests.get(
    "http://ec2-34-203-42-249.compute-1.amazonaws.com/token").json()['abi']

token_bytecode = requests.get(
    "http://ec2-34-203-42-249.compute-1.amazonaws.com/token").json()['bytecode']

ttBank_goerli_address = requests.get(
    "http://ec2-34-203-42-249.compute-1.amazonaws.com/ttbank").json()['addresses']['goerli']

ttBank_abi = requests.get(
    "http://ec2-34-203-42-249.compute-1.amazonaws.com/ttbank").json()['abi']

ttBank_bytecode = requests.get(
    "http://ec2-34-203-42-249.compute-1.amazonaws.com/ttbank").json()['bytecode']
