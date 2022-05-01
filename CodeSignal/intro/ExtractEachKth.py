'''
Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].
'''

def solution1(inputArray, k):
    del inputArray[k-1::k]
    return inputArray

def solution(inputArray, k):
    for i in range(len(inputArray) - 1, -1, -1):
        if (i + 1) % k == 0:
            inputArray.pop(i)
    return inputArray


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
