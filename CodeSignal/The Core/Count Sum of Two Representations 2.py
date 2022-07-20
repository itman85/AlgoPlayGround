'''
Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

Example

For n = 6, l = 2, and r = 4, the output should be
solution(n, l, r) = 2.

There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.
'''


def solution(n, l, r):
    count = 0
    for i in range(l, n//2 + 1):
        if n - i <= r:
            count += 1
    return count


def solution2(n, l, r):
    return sum(1 for a in range(l, r+1) if l <= a <= n - a <= r)