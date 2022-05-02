'''
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
solution(text) = "steady".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string text

Guaranteed constraints:
4 ≤ text.length ≤ 50.

[output] string

The longest word from text. It's guaranteed that there is a unique output.
'''


def isEnglishLetter(ch):
    return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'


def solution(text):
    fI, lI, mfI, mlI = -1, 0, 0, 0
    for i in range(len(text)):
        if isEnglishLetter(text[i]):
            if fI == -1:
                fI = i
            lI = i
            if mlI - mfI < lI - fI:
                mfI, mlI = fI, lI
        else:
            fI, lI = -1, 0
    return text[mfI:mlI + 1]

import re
def solution1(text):
    return max(re.split('[^a-zA-Z]', text), key=len)

import string
def solution2(t):
    return max("".join([i if i in string.ascii_letters else " " for i in t]).split(),key=len)

#Tips: max with key: len, int for ex find max digit in number:
# n = 123445
# print(max([i for i in str(n)],key=int))

print(solution("Ready, steady, go!"))
