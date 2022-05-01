'''
https://app.codesignal.com/arcade/intro/level-11/pwRLrkrNpnsbgMndb
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

'''


def solution(cell):
    cell = cell.lower()
    count = 0
    if ord('a') <= ord(cell[0]) + 1 <= ord('h') and 1 <= int(cell[1]) + 2 <= 8:
        count += 1
    if ord('a') <= ord(cell[0]) + 2 <= ord('h') and 1 <= int(cell[1]) + 1 <= 8:
        count += 1
    if ord('a') <= ord(cell[0]) + 2 <= ord('h') and 1 <= int(cell[1]) - 1 <= 8:
        count += 1
    if ord('a') <= ord(cell[0]) + 1 <= ord('h') and 1 <= int(cell[1]) - 2 <= 8:
        count += 1
    if ord('a') <= ord(cell[0]) - 1 <= ord('h') and 1 <= int(cell[1]) - 2 <= 8:
        count += 1
    if ord('a') <= ord(cell[0]) - 2 <= ord('h') and 1 <= int(cell[1]) - 1 <= 8:
        count += 1
    if ord('a') <= ord(cell[0]) - 2 <= ord('h') and 1 <= int(cell[1]) + 1 <= 8:
        count += 1
    if ord('a') <= ord(cell[0]) - 1 <= ord('h') and 1 <= int(cell[1]) + 2 <= 8:
        count += 1
    return count

# Tips: sum boolean (True = 1, False = 0) e.x: sum([True,False,True,True])  = 3
def solution1(cell):
    c = [ord(cell[0]) - 96, int(cell[1])]
    m = [[1, 2], [2, 1], [1, -2], [-2, 1], [-1, 2], [2, -1], [-1, -2], [-2, -1]]
    return sum([0 < c[0] + i[0] < 9 and 0 < c[1] + i[1] < 9 for i in m])


def solution2(c):
    x, y = ord(c[0]) - 96, int(c[1])
    return sum([1 <= (x + i) <= 8 and 1 <= (y + j) <= 8 for i in [-2, -1, 1, 2] for j in [-2, -1, 1, 2]]) // 2

#print(sum([True,False,True,True]))