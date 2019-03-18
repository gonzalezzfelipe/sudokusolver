import copy
from unittest import TestCase

from sudokusolver.sudokusolver import SudokuSolver
from sudokusolver.exceptions import UnsolvableSudoku
from sudokusolver.utils import print_sudoku

SUDOKU = [
    [5, 3, None, None, 7, None, None, None, None],
    [6, None, None, 1, 9, 5, None, None, None],
    [None, 9, 8, None, None, None, None, 6, None],
    [8, None, None, None, 6, None, None, None, 3],
    [4, None, None, 8, None, 3, None, None, 1],
    [7, None, None, None, 2, None, None, None, 6],
    [None, 6, None, None, None, None, 2, 8, None],
    [None, None, None, 4, 1, 9, None, None, 5],
    [None, None, None, None, 8, None, None, 7, 9],
]


class TestSudokuSolver(TestCase):

    def setUp(self):
        super().setUp()
        self.sudoku = copy.deepcopy(SUDOKU)

    def test_tolists(self):
        expected_output = [
            [
                5, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
            [
                6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                1, 9, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9]],
            [
                8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3],
            [
                4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8,
                [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], 1],
            [
                7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6],
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 8,
                [1, 2, 3, 4, 5, 6, 7, 8, 9]],
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 1, 9,
                [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5],
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8,
                [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7,
                9],
        ]
        self.assertListEqual(
            expected_output, SudokuSolver._tolists(self.sudoku))

    def test_complete(self):
        input = [
            [[1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1]]]
        expected_output = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]
        SudokuSolver._complete(input)
        self.assertListEqual(expected_output, input)
        with self.assertRaises(UnsolvableSudoku):
            SudokuSolver._complete([[[]]])

    def test_filter(self):
        ls = [[1, 2, 3], 2, 3, 4]
        SudokuSolver._filter(ls)
        self.assertListEqual([[1], 2, 3, 4], ls)

    def test_filterrows(self):
        ls = [[[1, 2, 3], 2, 3, 4]]
        SudokuSolver._filterrows(ls)
        self.assertListEqual([[[1], 2, 3, 4]], ls)

    def test_filtercols(self):
        ls = [
            [[1, 2, 3], 2],
            [3, 4]]
        SudokuSolver._filtercols(ls)
        self.assertListEqual([[[1, 2], 2], [3, 4]], ls)

    def test_filterblocks(self):
        sudoku = [
            [5, 3, [1, 2, 3, 5, 6], 1, 7, 1, 1, 1, 1],
            [6, 1, 1, 1, 9, 5, 1, 1, 1],
            [1, 9, 8, 1, 1, 1, 1, 6, 1],
            [8, 1, 1, 1, 6, 1, 1, 1, 3],
            [4, 1, 1, 8, 1, 3, 1, 1, 1],
            [7, 1, 1, 1, 2, 1, 1, 1, 6],
            [1, 6, 1, 1, 1, 1, 2, 8, 1],
            [1, 1, 1, 4, 1, 9, 1, [1, 2, 3, 7, 8, 9], 5],
            [1, 1, 1, 1, 8, 1, 1, 7, 9],
        ]
        SudokuSolver._filterblocks(sudoku)
        self.assertListEqual(
            [
                [5, 3, [2], 1, 7, 1, 1, 1, 1],
                [6, 1, 1, 1, 9, 5, 1, 1, 1],
                [1, 9, 8, 1, 1, 1, 1, 6, 1],
                [8, 1, 1, 1, 6, 1, 1, 1, 3],
                [4, 1, 1, 8, 1, 3, 1, 1, 1],
                [7, 1, 1, 1, 2, 1, 1, 1, 6],
                [1, 6, 1, 1, 1, 1, 2, 8, 1],
                [1, 1, 1, 4, 1, 9, 1, [3], 5],
                [1, 1, 1, 1, 8, 1, 1, 7, 9],
            ],
            sudoku)

    def test_check(self):
        ls = [[1, 3], [2, 5], [1, 4, 5]]
        SudokuSolver._check(ls)
        self.assertListEqual([[3], [2], [4]], ls)

    def test_checkrows(self):
        ls = [[[1, 3], [2, 5], [1, 4, 5]]]
        SudokuSolver._checkrows(ls)
        self.assertListEqual([[[3], [2], [4]]], ls)

    def test_checkcols(self):
        ls = [[[1, 3]], [[2, 5]], [[1, 4, 5]]]
        SudokuSolver._checkcols(ls)
        self.assertListEqual([[[3]], [[2]], [[4]]], ls)

    def test_checkblocks(self):
        sudoku = [
            [5, 3, [1, 2, 3, 5, 6], 1, 7, 1, 1, 1, 1],
            [6, [1, 2, 3, 5, 6, 7], 1, 1, 9, 5, 1, 1, 1],
            [1, 9, 8, 1, 1, 1, 1, 6, 1],
            [8, 1, 1, 1, 6, 1, 1, 1, 3],
            [4, 1, 1, 8, 1, 3, 1, 1, 1],
            [7, 1, 1, 1, 2, 1, 1, 1, 6],
            [1, 6, 1, 1, 1, 1, 2, 8, 1],
            [1, 1, 1, 4, 1, 9, 1, [1, 2, 3, 7, 8, 9], 5],
            [1, 1, 1, 1, 8, 1, 1, 7, [1, 2, 3, 7, 8]],
        ]
        SudokuSolver._checkblocks(sudoku)
        self.assertListEqual(
            [
                [5, 3, [1, 2, 3, 5, 6], 1, 7, 1, 1, 1, 1],
                [6, [7], 1, 1, 9, 5, 1, 1, 1],
                [1, 9, 8, 1, 1, 1, 1, 6, 1],
                [8, 1, 1, 1, 6, 1, 1, 1, 3],
                [4, 1, 1, 8, 1, 3, 1, 1, 1],
                [7, 1, 1, 1, 2, 1, 1, 1, 6],
                [1, 6, 1, 1, 1, 1, 2, 8, 1],
                [1, 1, 1, 4, 1, 9, 1, [9], 5],
                [1, 1, 1, 1, 8, 1, 1, 7, [1, 2, 3, 7, 8]],
            ],
            sudoku)