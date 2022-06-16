import pytest
from service.account_service import check_account_type

# Test if reterns right value for account
@pytest.mark.parametrize("input, expected", [
    (1, False), (3, False)
])
def test_check_account_type(input, expected):
    assert check_account_type(input) == expected