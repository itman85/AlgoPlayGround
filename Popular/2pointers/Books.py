'''
https://codeforces.com/problemset/problem/279/B

Input
The first line contains two integers n and t (1 ≤ n ≤ 105; 1 ≤ t ≤ 109) — the number of books and the number of free minutes Valera's got. The second line contains a sequence of n integers a1, a2, ..., an (1 ≤ ai ≤ 104), where number ai shows the number of minutes that the boy needs to read the i-th book.

Output
Print a single integer — the maximum number of books Valera can read.

input
4 5
3 1 2 1
output
3

input
3 3
2 2 3
output
1
'''

# O(2N)
def solution(n, t, a):
    l, maxl, maxr = 0, 0, -1
    for i in range(n):
        if sum(a[l:i + 1]) > t:
            l += 1
        if maxr - maxl < i - l:
            maxl, maxr = l, i
    print(f'{maxl} : {maxr}')
    return maxr - maxl + 1

# O(N)
def solution2(n, t, a):
    ans, sum, l = 0, 0, 0
    for r in range(n):
        sum += a[r]
        while sum > t:
            sum -= a[l]
            l += 1
        ans = max(ans, r - l + 1)
    return  ans


# print(solution(10, 8, [3, 4, 2, 2, 4, 3, 1, 1, 2, 3]))

# print(solution(10, 1, [3, 4, 2, 2, 4, 3, 2, 1, 2, 3]))

print(solution2(10, 3, [1, 1, 1, 4, 4, 5, 0, 0, 1, 1]))
