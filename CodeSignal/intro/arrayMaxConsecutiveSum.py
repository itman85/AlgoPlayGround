'''
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
solution(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
'''


def solution(inputArr, k):
    maxSum = 0
    lastSum = 0
    for i in range(len(inputArr) - k + 1):
        if lastSum == 0:
            lastSum = sum(inputArr[i:i + k])
        else:
            lastSum = lastSum - inputArr[i - 1] + inputArr[i + k - 1]
        if lastSum > maxSum:
            maxSum = lastSum
    return maxSum


def solution1(a, k):
    c = m = sum(a[:k])
    for i in range(len(a) - k):
        c = c + a[i + k] - a[i]
        m = max(c, m)

    return m

inputArr = [1, 3, 2, 4]
print(sum(inputArr))
print(solution1(inputArr, 3))
