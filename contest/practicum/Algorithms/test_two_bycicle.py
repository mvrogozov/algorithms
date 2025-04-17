import pytest
from two_bycicle import get_buy_day2

@pytest.mark.parametrize('input_data, result', [
    (
        (0, 6, [1, 2, 4, 4, 5, 6], 3),
        (3)
    ),
    (
        (0, 0, [3], 3),
        (1)
    ),
    (
        (0, 6, [1, 2, 4, 4, 5, 6], 6),
        (6)
    ),
    (
        (0, 5, [1, 2, 4, 4, 5, 6], 7),
        (-1)
    )
])
def test_2_bycicle(input_data, result):
    print(*input_data)
    assert get_buy_day2(*input_data) == result, 'answer wrong'
