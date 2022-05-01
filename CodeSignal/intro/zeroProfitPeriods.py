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


print(solution([1, 1, 2, -3, 0, 1000, 6, -6, 1, 1, 1, -3, 2]))
