'''
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
solution(n) = 52;
For n = 1001, the output should be
solution(n) = 101.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
10 ≤ n ≤ 10^6.

[output] integer
'''

# this solution if left digit < right digit then remove left digit, if not find them remove last digit
def solution(n):
    strN = str(n)
    for i in range(1, len(strN)):
        if strN[i] > strN[i - 1]:
            return int(strN[:i - 1] + strN[i:])
    return int(strN[:-1])

# this solution compare all value (by remove at i in 0 -> len -1) to find max
def solution1(n):
    n = str(n)
    return max(int(''.join(n[:i]+n[i+1:])) for i in range(len(n)))

print(solution(3210))
