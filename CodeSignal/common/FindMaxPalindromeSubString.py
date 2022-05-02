'''
find max palindrome substring in a given string
for ex string s = "abcdeabcecbaeaefffdf"
return "abcecba"
'''

# O(n^2), can use suffix array to improve O(N*logN)
def solution(s):
    mlo, mup = 0, 0
    n = len(s)
    # F[i][j] = true if substring s[i:j] is palindrome, otherwise false
    F = [[False] * n for i in range(n)]  # F[i][i] = True (len = 1), F[i][j] = F[i+1][j-1] and s[i]=s[j]
    for i in range(n):
        F[i][i] = True  # all substrings have len = 1 is palindrome -> set = True
    for L in range(2, n + 1):  # loop len substring from 2 -> n
        for i in range(n - (L - 1)):
            j = i + (L - 1)  # index start from 0 so it needs to minus 1 for L (len)
            F[i][j] = F[i + 1][j - 1] and s[i] == s[j]
            if F[i][j] and mup - mlo < j - i:
                mlo, mup = i, j
    if mup - mlo > 0:
        return s[mlo:mup + 1]
    else:
        return ""  # not found any palindrome substring

# print(solution("0123456"))
# print(solution("101232141"))
print(solution("abcdeabcecbaeaeffffdf"))
