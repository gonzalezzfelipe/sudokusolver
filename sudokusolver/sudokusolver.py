import copy
from collections import Counter

from sudokusolver.exceptions import UnsolvableSudoku
from sudokusolver.utils import (
    assert_correct_format, yield_possibility, print_sudoku, flatten)


class SudokuSolver:

    @staticmethod
    def _tolists(sudoku):
        """Turn Nones to lists."""
        return [
            [[i for i in range(1, 10)] if element is None
             else element for element in row]
            for row in sudoku]

    @staticmethod
    def _complete(sudoku):
        """Convert lists with only one element to ints."""
        for i in range(9):
            for j in range(9):
                if isinstance(sudoku[i][j], list):
                    if len(sudoku[i][j]) == 1:
                        sudoku[i][j] = sudoku[i][j][0]
                    elif len(sudoku[i][j]) == 0:
                        raise UnsolvableSudoku(
                            'Sudoku cannot be solved, no valid value to'
                            'place on position {i}, {j}.'.format(i=i, j=j))

    @staticmethod
    def _yield_blocks(sudoku):
        """Yield 3x3 blocks in sudoku."""
        for i in range(3):
            for j in range(3):
                yield [
                    element
                    for row in sudoku[3 * i: 3 * i + 3]
                    for element in row[3 * i: 3 * i + 3]]

    @staticmethod
    def _filter(ls):
        """Filter ints in list of lists."""
        ints = [a for a in ls if isinstance(a, int)]
        for element in ls:
            if isinstance(element, list):
                for _int in ints:
                    try:
                        element.remove(_int)
                    except ValueError:  # Element was already removed
                        pass

    @staticmethod
    def _filterrows(sudoku):
        """Filter elements if repeated in row."""
        for row in sudoku:
            SudokuSolver._filter(row)

    @staticmethod
    def _filtercols(sudoku):
        """Filter elements if repeated in column."""
        for column in zip(*sudoku):
            SudokuSolver._filter(column)

    @staticmethod
    def _filterblocks(sudoku):
        """Filter elements if repeated in block."""
        for block in SudokuSolver._yield_blocks(sudoku):
            SudokuSolver._filter(block)

    @staticmethod
    def _check(ls):
        """Check elements in lists of ls cant be anywhere else."""
        lists = [element for element in ls if isinstance(element, list)]
        flattened = flatten(lists)
        unique = {k: v for k, v in Counter(flattened).items() if v == 1}
        for value in unique.keys():
            for element in lists:
                if value in element:
                    element.clear()
                    element.append(value)

    @staticmethod
    def _checkrows(sudoku):
        """Confirm elements in a row cant be in anywhere else."""
        for row in sudoku:
            SudokuSolver._check(row)

    @staticmethod
    def _checkcols(sudoku):
        """Confirm elements in a row cant be in anywhere else."""
        for col in zip(*sudoku):
            SudokuSolver._check(col)

    @staticmethod
    def _checkblocks(sudoku):
        """Confirm elements in a row cant be in anywhere else."""
        for block in SudokuSolver._yield_blocks(sudoku):
            SudokuSolver._check(block)

    @staticmethod
    def base_routine(sudoku):
        """Apply basic routine on sudoku.

        This means checking for repeated values in rows, columns, and
        blocks and doing this until no more changes can be done without
        guessing."""
        _check_equal = None
        while _check_equal != sudoku:
            _check_equal = copy.deepcopy(sudoku)
            SudokuSolver._filterrows(sudoku)
            SudokuSolver._filtercols(sudoku)
            SudokuSolver._filterblocks(sudoku)
            SudokuSolver._checkrows(sudoku)
            SudokuSolver._checkcols(sudoku)
            SudokuSolver._checkblocks(sudoku)
            SudokuSolver._complete(sudoku)

    @staticmethod
    def is_solved(sudoku):
        """Return True if the sudoku is solved."""
        return all([
            isinstance(element, int) for row in sudoku for element in row])

    @staticmethod
    def _solve(sudoku):
        """Sudoku with iterative approach."""
        SudokuSolver.base_routine(sudoku)
        if not SudokuSolver.is_solved(sudoku):
            for _sudoku in yield_possibility(sudoku):
                try:
                    sudoku = SudokuSolver._solve(_sudoku)
                    break
                except UnsolvableSudoku:
                    pass
            raise UnsolvableSudoku('Sudoku could not be solved.')
        else:
            return sudoku

    def solve(self, sudoku, inplace=False):
        """Solve sudoku.

        The SUDOKU should be a list of 9 lists, containing 9 elements.
        The unknown spaces should be None, and the rest ints.

        Usage
        -----
        ```python
        from sudokusolver import SudokuSolver

        sudoku = [
            [None, 6, None, 3, None, None, 8, None, 4],
            [5, 3, 7, None, 9, 5, None, None, None],
            [None, 4, None, None, None, 6, 3, None, 7],
            [None, 9, None, None, 5, 1, 2, 3, 8],
            [4, None, None, 8, None, 3, None, None, 1],
            [7, None, None, None, 2, None, None, None, 6],
            [None, 6, None, None, None, None, 2, 8, None],
            [None, None, None, 4, 1, 9, None, None, 5],
            [None, None, None, None, 8, None, None, 7, 9],
        ]
        solver = SudokuSolver()
        solved = solver.solve(sudoku)
        ```

        Parameters
        ----------
        sudoku : list of lists
            Sudoku to solve, should follow logic described above.
        inplace : boolean, optional, default : False
            Whether to make the changes on the same list or to return a
            new one.

        """
        assert_correct_format(sudoku)
        if inplace:
            sudoku = copy.copy(sudoku)
        sudoku = self._tolists(sudoku)
        return SudokuSolver._solve(sudoku)


if __name__ == '__main__':

    solver = SudokuSolver()
    solved = solver.solve(sudoku)
