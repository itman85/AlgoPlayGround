'''
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

solution(n) = [[1, 2, 3],
               [8, 9, 4],
               [7, 6, 5]]
'''

# ideas: set value for each of 4 edges of square size k
def solution(n):
    # init 2D array with value 0
    sq = [[0 for i in range(n)] for j in range(n)]
    count = 1
    for k in range(1, n // 2 + n % 2 + 1, 1):
        for col in range(k - 1, n - k, 1):
            if sq[k - 1][col] == 0:
                sq[k - 1][col] = count
                count += 1
        for row in range(k - 1, n - k, 1):
            if sq[row][n - k] == 0:
                sq[row][n - k] = count
                count += 1
        for col in range(n - k, -1, -1):
            if sq[n - k][col] == 0:
                sq[n - k][col] = count
                count += 1
        for row in range(n - k, -1, -1):
            if sq[row][k - 1] == 0:
                sq[row][k - 1] = count
                count += 1
    return sq


def solution1(n, m=0, s=1):
    if m == 0: m = n
    if n == 1 == m:
        return [[s]]

    # Calculate spiral numbers without first row
    S = solution1(m - 1, n, s + n)

    # Create first row and add the transpose of the rest
    return [range(s, s + n)] + zip(*S[::-1])

def solution2(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m

print(solution1(4))

''' 
k = 6: 0,0 > 5; 0 > 5, 5; 5, 5> 0; 5 > 0,0
k = 4: 1,1>4; 1>4,4; 4, 4>0; 4>0, 0 
k = 2: 2,2>3; 2>3,3 , 3,3>2, 3>2,2
'''
