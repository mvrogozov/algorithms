import pytest
from calculator import EmptyStackException, calculator as calc


@pytest.mark.parametrize('input_data, result', [
    (['1', '2', '+'], 3),
    (['3', '4', '*'], 12),
])
def test_calculator(input_data, result):
    assert calc(input_data) == result, 'arithmetic wrong'


def test_calculator_empty_input():
    with pytest.raises(EmptyStackException):
        calc([])
