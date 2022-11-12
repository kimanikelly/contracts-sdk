import requests

x = requests.get(
    "https://kimanikelly-contractapi.herokuapp.com/tokenContract").json()

print(x)
