'''
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
solution(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
solution(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
solution(inputString) = false.
'''


def isHexadecimalDigit(ch):
    return '0' <= ch <= '9' or 'A' <= ch <= 'F'


def solution(inputString):
    lst = inputString.split('-')
    if len(lst) != 6:
        return False
    else:
        for g in lst:
            if not (isHexadecimalDigit(g[0]) and isHexadecimalDigit(g[1]) if len(g) == 2 else False):
                return False
        return True


import re


def solution1(s):
    return bool(re.match(('^' + '[\dA-F]{2}-' * 6)[:-1] + '$', s))


def solution2(inputString):
    try:
        all = inputString.split('-')
        if len(all) != 6:
            return False
        for s in all:
            if len(s) != 2:
                return False
            int(s, 16)
        return True
    except:
        return False


print(solution("FF-FF-FF-FF-FF-FF"))
