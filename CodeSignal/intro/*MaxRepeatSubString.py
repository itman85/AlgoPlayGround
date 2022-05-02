'''
find max repeat substring in a given string
for ex string s = "abcdeaaaaaeeefffedf"
return "aaaaa"
'''
# Ideas: move range [lo,up] to find max repeat substring, then store index in (finlo,finup)
def solution(s):
    lo, up, finlo, finup = 0, 1, 0, 1
    # O(n)
    while up < len(s):
        if s[up] != s[up - 1]:
            if finup - finlo < up - lo:
                finlo, finup = lo, up  # update new bigger range for repeating chars
            lo = up
        up += 1
    if finup - finlo < up - lo:
        finlo, finup = lo, up  # update new bigger range for repeating chars
    return s[finlo:finup]

print(solution("abcdeaaaaaeeefffedf"))