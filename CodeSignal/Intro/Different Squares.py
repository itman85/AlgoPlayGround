'''
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
solution(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix

Guaranteed constraints:
1 ≤ matrix.length ≤ 100,
1 ≤ matrix[i].length ≤ 100,
0 ≤ matrix[i][j] ≤ 9.

[output] integer

The number of different 2 × 2 squares in matrix.
'''


def solution(matrix):
    nRow = len(matrix)
    nCol = len(matrix[0])
    lst = []
    for row in range(nRow):
        for col in range(nCol):
            if row + 1 < nRow and col + 1 < nCol:
                temp = " ".join(str(matrix[i][j]) for i in [row, row + 1] for j in [col, col + 1])
                if temp not in lst:
                    lst.append(temp)
    return len(lst)

def solution1(matrix):
    s = set()
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
                s.add((matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]))
    return len(s)

# Tips: create set and add item into set, it will auto make each item is different in set