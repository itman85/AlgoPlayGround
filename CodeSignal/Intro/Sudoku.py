'''
https://app.codesignal.com/arcade/intro/level-12/tQgasP8b62JBeirMS
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
solution(grid) = true;

For
grid = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
        [4, 6, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
solution(grid) = false.

The output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
These examples are represented on the image below.



Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer grid

A matrix representing 9 × 9 grid already filled with numbers from 1 to 9.

Guaranteed constraints:
grid.length = 9,
grid[i].length = 9,
1 ≤ grid[i][j] ≤ 9.

[output] boolean

true if the given grid represents a correct solution to Sudoku, false otherwise.
'''


def solution(grid):
    for row in range(0, 9):
        lst = []
        for col in range(0, 9):
            if grid[row][col] not in lst:
                lst.append(grid[row][col])
            else:
                return False
    for col in range(0, 9):
        lst = []
        for row in range(0, 9):
            if grid[row][col] not in lst:
                lst.append(grid[row][col])
            else:
                return False
    for sgRow in range(0, 3):
        for sgCol in range(0, 3):
            lst = []
            for i in range(0, 9):
                if grid[sgRow * 3 + i // 3][sgCol * 3 + i % 3] not in lst:
                    lst.append(grid[sgRow * 3 + i // 3][sgCol * 3 + i % 3])
                else:
                    return False
    return True


def solution1(grid):
    def r(i):
        return sorted(grid[i]) != list(range(1, 10))

    def c(i):
        return sorted([grid[x][i] for x in range(9)]) != list(range(1, 10))

    def g(x, y):
        return sorted([grid[i][j] for i in range(x, x + 3) for j in range(y, y + 3)]) != list(range(1, 10))

    for i in range(9):
        if r(i) or c(i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if g(i, j):
                return False
    return True


'''
bool solution(std::vector<std::vector<int>> grid) {
    for (int i = 0; i < 9; i++) {
        int a = 0, b = 0, c = 0;
        for (int j = 0; j < 9; j++) {
            a ^= 1 << grid[i][j];
            b ^= 1 << grid[j][i];
            c ^= 1 << grid[i - i % 3 + j / 3][i % 3 * 3 + j % 3];
        }
        if (a != 1022 || b != 1022 || c != 1022)
            return false;
    }
    return true;
}
'''
