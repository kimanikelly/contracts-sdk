from src.utils import *


def test_ttBank_addresses_rinkeby():
    assert ttBank_addresses(42) == "0xfbBb2A07F7a38CDB3025CE91acd94Ab74c4DCc50"
