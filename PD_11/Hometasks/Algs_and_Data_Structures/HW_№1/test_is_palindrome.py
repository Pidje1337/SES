from HW_1 import is_palindrome
import pytest

@pytest.mark.parametrize("num, expected_result",
                         [
                             (11, True),
                             (1001, True),
                             (1234, False),
                             (121, True),
                             (14641, True),
                             (178, False)
                         ])
def test_is_palindrome(num, expected_result):
    assert is_palindrome(num) == expected_result