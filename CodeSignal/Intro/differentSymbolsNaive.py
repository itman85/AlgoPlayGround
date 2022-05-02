'''
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
solution(s) = 3.

There are 3 different characters a, b and c.
'''


def solution(s):
    chDict = {}
    for ch in s:
        if ch not in chDict:
            chDict[ch] = ch
    return len(chDict)


def solution(s):
    return len(set(s))


str1 = "cabca"
print(set(str1))  # >>> {'c', 'b', 'a'}
print(list(str1))  # >>> ['c', 'a', 'b', 'c', 'a']
print(tuple(str1))  # >>> ('c', 'a', 'b', 'c', 'a')