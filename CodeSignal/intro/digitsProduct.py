'''
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
solution(product) = 26;
For product = 19, the output should be
solution(product) = -1.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer product

Guaranteed constraints:
0 ≤ product ≤ 600.

[output] integer
'''

# idea: divide product for number index from 9 -> 2 and add index number into head of lst
def solution(product):
    if product == 0:
        return 10
    if product == 1:
        return 1
    lst = ""
    index = 9
    while index > 1:
        if product % index == 0:
            lst = str(index) + lst
            product = product // index
        else:
            index -= 1
    return -1 if product != 1 else int(lst)

print(solution(581))
