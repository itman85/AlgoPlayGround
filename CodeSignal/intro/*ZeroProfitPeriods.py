'''
Lindsey, a small fox, has a bank account. She has a list of her transactions during some period of time. Negative transactions[i] means that the money leaves the account, and positive transactions[i] means that money is added to the account.

Lindsey refers to the sum of consecutive transactions as the profit of these transactions. She wants to find the maximum number of non-overlapping periods of consecutive transactions with zero profit. Please, help the fox.

Example

For transactions = [1, 1, 2, -3, 0, 1000, 6, -6, 1, 1, 1, -3, 2], the output should be
solution(transactions) = 4.

The periods [1, 2, -3], [0], [6, -6], [1, 1, 1, -3] are each zero-profit. Also, the periods [1, 2, -3], [0], [6, -6], [1, -3, 2] are zero-profit as well.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer transactions

A list of Lindsey's bank transactions, in chronological order. Positive values represent deposits, and negative values represent withdrawals.

Guaranteed constraints:
1 ≤ transactions.length ≤ 105,
-103 ≤ transactions[i] ≤ 103.

[output] integer

The maximum number of non-overlapping periods of consecutive transactions with zero profit.
'''

'''
Idea:
transactions = [a1,a2,a3,...aN]
s1= a1
s2 = a1+a2
s3 = a1+a2+a3
...
si = a1+a2+...ai
if si + a[i+1] = sj  1 <= j < i
=> a[j+1] + ...  + ai = 0
'''


def findInList(lst, fi):
    for i in range(len(lst)):
        if lst[i] == fi:
            return i
    return -1


# O(n^2) can use binary tree to improve findInList???
def solution(transactions):
    sumSubPeriods = []
    count = 0
    for i in range(len(transactions)):
        if transactions[i] == 0:
            count += 1
            sumSubPeriods = []
        else:
            if len(sumSubPeriods) == 0:
                sumSubPeriods.append(transactions[i])
            else:
                sumi = sumSubPeriods[-1] + transactions[i]
                if findInList(sumSubPeriods, sumi) != -1 or sumi == 0:
                    count += 1
                    sumSubPeriods = []
                else:
                    sumSubPeriods.append(sumi)
    return count


# #O(n*logn) dynamic programming
def solution2(transactions):
    sumN = [0] * len(transactions)
    sumN[0] = transactions[0]
    f = [0] * len(
        transactions)  # f[i] is max zero profile periods from 0 to i, f[i] = max(f[i-1],f[j]+1) with j nearest i (j<i) where sumN[j] = sumN[i]
    f[0] = int(transactions[0] == 0)
    d = {transactions[0]: 0}  # key is sum from 0 to i, value is index i
    # O(n)
    for i in range(1, len(transactions)):
        sumN[i] = sumN[i - 1] + transactions[i]  # sumN[i] = sum(transactions[:i])

    # O(n*logn)
    for i in range(1, len(transactions)):
        f[i] = f[i - 1]
        if transactions[i] == 0:
            f[i] += 1
        elif sumN[i] == 0 and f[i] == 0:  # f[i] == 0 to make sure from 0 -> i non-overlapping zero periods
            f[i] = 1
        elif sumN[i] in d.keys():  # find key in dict 0(logn)
            j = d[sumN[i]]
            f[i] = max(f[i], f[j] + 1)
        d[sumN[i]] = i
    return f[-1]


def solution3(transactions):
    sumN = []
    sumN.append(transactions[0])
    f = []  # f[i] is max zero profile periods from 0 to i
    f.append(int(transactions[0] == 0))
    d = {transactions[0]: 0}  # key is sum from 0 to i, value is index i
    # O(n)
    for i in range(1, len(transactions)):
        sumN.append(sumN[-1] + transactions[i])

    # O(n*logn)
    for i in range(1, len(transactions)):
        f.append(f[i - 1])
        if transactions[i] == 0:
            f[-1] += 1
        elif sumN[i] == 0 and f[-1] == 0:  # f[i] == 0 to make sure from 0 -> i non-overlapping zero periods
            f[-1] = 1
        elif sumN[i] in d.keys():  # find key in dict 0(logn)
            j = d[sumN[i]]
            f[-1] = max(f[-1], f[j] + 1)
        d[sumN[i]] = i
    return f[-1]


print(solution3([1, 1, 2, -3, 0, 1000, 6, -6, 1, 1, 1, -3, 2]))
# print(solution2([6, -6, 1, 0, 0, -1]))
