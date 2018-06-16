import pytest

import {{ cookiecutter.project_slug }}


@pytest.mark.parametrize("test_input, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
])
def test_fib(test_input, expected):
    '''
    test fib
    '''
    assert {{ cookiecutter.project_slug }}.fib(test_input) == expected
