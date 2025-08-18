from HW_1 import fibonacci
import pytest

@pytest.mark.parametrize("num, expected_result",
                         [
                             (0, 1),
                             (1, 1),
                             (4, 5),
                             (6, 13),
                             (8, 34)
                         ])
def test_fibonacci(num, expected_result):
    assert fibonacci(num) == expected_result