'''
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
solution(inputArray) = false.

There are 6 possible arrangements for these strings:

["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be
solution(inputArray) = true.

It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.
'''

# Tips: zip , copy string, pop item from list
def check2StringsDiffExactOneChar(str1, str2):
    return sum([a[0] != a[1] for a in zip(str1, str2)]) == 1


def findNextArrangement(fItem, itemsSet):
    if len(itemsSet) == 0:
        return True
    for i in range(0, len(itemsSet), 1):
        if check2StringsDiffExactOneChar(fItem, itemsSet[i]):
            tempSet = itemsSet.copy()
            tempSet.pop(i)
            if findNextArrangement(itemsSet[i], tempSet):
                return True
    return False


def solution(inputArrs):
    for i in range(len(inputArrs)):
        subSet = inputArrs.copy()
        subSet.pop(i)
        if findNextArrangement(inputArrs[i], subSet):
            return True
    return False


arrayStrs = ["ab", "bb", "aa"]#["aba", "bbb", "bab"]
print(arrayStrs)
if solution(arrayStrs):
    print("Yes")
else:
    print("No")
