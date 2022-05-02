'''
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
solution(s) = "2a3bc".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

String consisting of lowercase English letters.

Guaranteed constraints:
4 ≤ s.length ≤ 15.

[output] string

Encoded version of s.
'''


def solution(s):
    lst = [[s[0]]]
    for i in range(1, len(s)):  # s.length >= 4
        if s[i] != s[i - 1]:
            lst.append([s[i]])
        else:
            lst[-1].append(s[i])
    res = ""
    for s1 in lst:
        if len(s1) > 1:
            res += str(len(s1)) + s1[0]
        else:
            res += s1[0]
    return res


import re


def solution1(s):
    counted = re.findall(r'((\w)\2*)', s)
    return "".join([str(len(count[0])) + count[1] if len(count[0]) > 1 else str(count[0]) for count in counted])
