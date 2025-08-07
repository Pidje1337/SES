from HW_1 import factorial
import pytest

@pytest.mark.parametrize("num, expected_result",
                         [
                             (0, 1),
                             (2, 2),
                             (5, 120),
                             (7, 5040),
                             (10, 3_662_800)
                          ])
def test_factorial(num, expected_result):
    assert factorial(num) == expected_result