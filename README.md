# contracts-sdk

[![Python application](https://github.com/kimanikelly/ttBank-sdk-python/actions/workflows/python-app.yml/badge.svg)](https://github.com/kimanikelly/ttBank-sdk-python/actions/workflows/python-app.yml)
[![Publish Python 🐍 distributions 📦 to PyPI and TestPyPI](https://github.com/kimanikelly/contracts-sdk/actions/workflows/python-publish.yml/badge.svg)](https://github.com/kimanikelly/contracts-sdk/actions/workflows/python-publish.yml)

## Summary

The goal of this Software Development Kit was to build accessible abstractions from the [Smart Contracts](https://github.com/kimanikelly/contracts) repository as Python Classes that can be easily installed in a server-side environment and allow communication between the Off-Chain applications and Ethereum compatible protocols. The Smart Contract instances are pre-built through [Contracts-API](https://github.com/kimanikelly/contracts-api), making it easier for a user to connect and perform read/write functionality in other projects.

## Test PyPI Package Installation

```
pip install -i https://test.pypi.org/simple/ smart-contracts-sdk
```

## Source Code Installation

```
git clone https://github.com/kimanikelly/contracts-sdk.git
```

## Source Code Dependency Installation

Main project build

```
pip install build
```

Install [Ganache](https://www.npmjs.com/package/ganache) for local source code testing

```
npm install ganache --global
```

## Source Code Testing

Open one terminal and run the command

```
ganache
```

Open another terminal and run the command

```
pytest
```

## Smart Contract Classes

The Off-Chain Class abstraction of [Token.sol](https://github.com/kimanikelly/contracts/blob/main/contracts/Token.sol)

- [Token](https://github.com/kimanikelly/contracts-sdk/blob/main/src/token_erc20.py)

The Off-Chain Class abstraction of [TTBank.sol](https://github.com/kimanikelly/contracts/blob/main/contracts/TTBank.sol)

- [TTBank](https://github.com/kimanikelly/contracts-sdk/blob/main/src/ttBank.py)
