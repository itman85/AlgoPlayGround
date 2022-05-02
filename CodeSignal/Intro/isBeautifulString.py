'''
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be solution(inputString) = true.

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be solution(inputString) = false.

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be solution(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.
'''


def solution(inputString):
    chDict = {}
    for ch in inputString:
        if ch not in chDict:
            chDict[ch] = 1
        else:
            chDict[ch] += 1
    for ch in chDict.keys():
        if (chr(ord(ch) - 1) in chDict and chDict[ch] > chDict[chr(ord(ch) - 1)]) or (
                chr(ord(ch) - 1) not in chDict and ord(ch) - 1 >= ord('a')):
            return False
    return True


import string


def solution1(inputString):
    r = [inputString.count(i) for i in string.ascii_lowercase]
    return r[::-1] == sorted(r)


def solution2(s):
    l = [s.count(i) for i in string.ascii_lowercase[::-1]]
    return l == sorted(l)


# Tip: letter previous a letter ('c) print(chr(ord('c')-1))
# print(string.ascii_lowercase)

print(solution1("bbbaacdafe"))
