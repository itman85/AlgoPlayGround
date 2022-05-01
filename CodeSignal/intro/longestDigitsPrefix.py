'''
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".
'''


def solution(inputString):
    for i in range(len(inputString)):
        if not inputString[i].isdigit():
            return inputString[:i]
    return inputString


import re


def solution1(inputString):
    return re.findall('^\d*', inputString)[0]


solution("0123456789")
