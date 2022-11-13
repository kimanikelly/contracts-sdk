from src.utils import *


def test_ttBank_addresses_goerli():
    assert ttBank_addresses(5) == "0xCD8B3F1bd2b96Bc5Aed9a2ac3Fc548a27acCc226"
