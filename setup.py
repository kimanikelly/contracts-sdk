from setuptools import setup, find_packages

VERSION = "1.0.0"
DESCRIPTION = "Smart Contract Software Development Kit"
LONG_DESCRIPTION = "A Software Development Kit interacting with Solidity Smart Contracts, aiming to build Off-Chain applications on Ethereum compatible protocols."

setup(
    name="Smart Contract SDK",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Kimani Kelly",
    author_email="kimanikelly95@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords="Smart Contract SDK"
)
