'''
https://app.codesignal.com/arcade/intro/level-9/6M57rMTFB9MeDeSWo
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:


Example

For bishop = "a1" and pawn = "c3", the output should be
solution(bishop, pawn) = true.



For bishop = "h1" and pawn = "h3", the output should be
solution(bishop, pawn) = false.


'''
'''
Tips: convert char to int and int to char
>>> chr(97)
'a'
>>> ord('a')
97
'''
def solution(bishop, pawn):
    return abs(ord(bishop[0])-ord(pawn[0])) == abs(ord(bishop[1])-ord(pawn[1]))

print(solution("h1","h3"))