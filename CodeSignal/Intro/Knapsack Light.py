'''
You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2.
What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

Example

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
solution(value1, weight1, value2, weight2, maxW) = 10.

You can only carry the first item.

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be
solution(value1, weight1, value2, weight2, maxW) = 16.

You're strong enough to take both of the items with you.

For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be
solution(value1, weight1, value2, weight2, maxW) = 7.

You can't take both items, but you can take any of them.
'''


def solution(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        if weight1 > maxW >= weight2:
            return value2
        elif weight2 > maxW >= weight1:
            return value1
        elif weight1 <= maxW and weight2 <= maxW:
            return max(value1, value2)
        else:
            return 0


def solution1(v1, w1, v2, w2, W):
    return max(int(w1 <= W) * v1, int(w2 <= W) * v2, int(w1 + w2 <= W) * (v1 + v2))


def solution2(v1, w1, v2, w2, maxW):
    return max(x for x, y in [(0, 0), (v1, w1), (v2, w2), (v1 + v2, w1 + w2)] if y <= maxW)


print(solution(15, 2, 20, 3, 2))

print(max(x for x in [1, 2, 3, 4, 5] if x > 3))
