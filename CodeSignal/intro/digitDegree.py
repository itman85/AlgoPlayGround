'''
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
solution(n) = 0;
For n = 100, the output should be
solution(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
solution(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
'''


def solution(n):
    count = 0
    while n > 9:
        count += 1
        n = sum([int(x) for x in str(n)])
    return count


def solution1(n):
    if n < 10:
        return 0
    sumOfDigits = sum([int(i) for i in str(n)])
    return solution1(sumOfDigits) + 1


# Tips: convert number to array. ex 123 -> [1,2,3]
# [int(x) for x in str(123)]
# print([int(x) for x in str(123)])

print(solution(91))
