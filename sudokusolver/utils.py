import copy
from itertools import repeat

from sudokusolver.exceptions import IncorrectSudokuFormat


def assert_correct_format(sudoku):
    """Assert sudoku is correctly defined."""
    if not len(sudoku) == 9:
        raise IncorrectSudokuFormat(
            f'Sudoku should contain 9 rows, not {len(sudoku)}.')
    for row in sudoku:
        if not len(row) == 9:
            raise IncorrectSudokuFormat(
                f'All rows should contain 9 elements.')
        for element in row:
            if not (isinstance(element, int) or element is None):
                raise IncorrectSudokuFormat(
                    'Elements should be None or int, not {type(element)}.')


def first(iterable, condition=lambda x: True):
    """
    Returns the first item in the `iterable` that
    satisfies the `condition`.

    If the condition is not given, returns the first item of
    the iterable.

    Raises `StopIteration` if no item satysfing the condition is found.

    >>> first( (1,2,3), condition=lambda x: x % 2 == 0)
    2
    >>> first(range(3, 100))
    3
    >>> first( () )
    Traceback (most recent call last):
    ...
    StopIteration
    """
    return next(x for x in iterable if condition(x))


def flatten(ls):
    return [i for sublist in ls for i in sublist]


def yield_possibility(sudoku):
    """Get different possibilities from sudoku."""
    flattened = flatten(sudoku)
    for i, item in enumerate(flattened):
        if isinstance(flattened[i], list):
            possibilities = copy.copy(flattened[i])
            break
    j = 0
    while j < len(possibilities):
        _sudoku = copy.deepcopy(sudoku)
        _sudoku[i // 9][i % 9] = possibilities[j]
        yield _sudoku
        j += 1


def print_sudoku(sudoku):
    """Pretty print sudoku."""

    def value_to_str(element):
        if isinstance(element, int):
            return str(element)
        else:
            return ' '

    print('|' + '|'.join(repeat('---', 9)) + '|')
    for row in sudoku:
        values = [' ' + value_to_str(element) + ' ' for element in row]
        print('|' + '|'.join(values) + '|')
        print('|' + '|'.join(repeat('---', 9)) + '|')
