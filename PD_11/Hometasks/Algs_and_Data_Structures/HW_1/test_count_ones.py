from HW_1 import count_ones
import pytest

@pytest.mark.parametrize("num, expected_result",
                         [
                             (2, 1),
                             (7, 3),
                             (9, 2),
                             (29, 4),
                             (89, 4)
                         ])
def test_count_ones(num: int, expected_result: int):
    assert count_ones(num) == expected_result