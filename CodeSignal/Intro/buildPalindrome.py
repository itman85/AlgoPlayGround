'''
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
solution(st) = "abcdcba".
'''


def isPalindromeString(str):
    return str == str[::-1]


def solution(st):
    for i in range(len(st)):
        temp = st + st[:i][::-1]  # ex i = 2 => "abcdc" + "abcdc"[:2][::-1] ( <=> "ba)
        if isPalindromeString(temp):
            return temp


solution("abcdc")
