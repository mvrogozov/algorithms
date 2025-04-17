import pytest
from matrix_trans import matrix_trans


@pytest.mark.parametrize('input_data, result', [
    (
        (3, 3,
            [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]),
        [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
    ),
    (
        (4, 3,
            [
                ['1', '2', '3'],
                ['4', '5', '6'],
                ['7', '8', '9'],
                ['10', '11', '12']
            ]),
        [['1', '4', '7', '10'], ['2', '5', '8', '11'], ['3', '6', '9', '12']]
    ),
    (
        (1, 2,
            [['1', '2']]),
        [['1'], ['2']]
    ),
])
def test_matrix_trans(input_data, result):
    assert matrix_trans(*input_data) == result, 'answer wrong'
