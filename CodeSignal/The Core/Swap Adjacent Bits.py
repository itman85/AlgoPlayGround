'''
You're given an arbitrary 32-bit integer n. Take its binary representation, split bits into it in pairs (bit number 0 and 1, bit number 2 and 3, etc.) and swap bits in each pair. Then return the result as a decimal number.

Example

For n = 13, the output should be
solution(n) = 14.

13 10 = 1101 2 ~> {11}{01} 2 ~> 1110 2 = 14 10.

For n = 74, the output should be
solution(n) = 133.

74 10 = 01001010 2 ~> {01}{00}{10}{10} 2 ~> 10000101 2 = 133 10.
Note the preceding zero written in front of the initial number: since both numbers are 32-bit integers, they have 32 bits in their binary representation. The preceding zeros in other cases don't matter, so they are omitted. Here, however, it does make a difference.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
0 ≤ n < 2^30.

[output] integer
'''

# tips: convert int to binary string: bin(n), swap bit in pairs  ((x & 0b1010) >> 1) || ((x & 0b0101) << 1)
def solution(n):
    fbit = 0xaaaaaaaa  # = 0b10101010101010101010101010101010
    sbit = 0x55555555  # = 0b01010101010101010101010101010101
    n = ((n & fbit) >> 1) | ((n & sbit) << 1)
    return n

print(solution(74))
'''
x = 13
print(bin(x))
keep first bit
x1 = (x & 0b1010)
print(bin(x1))
x1 = x1 >> 1
print(bin(x1))

keep second bit
x2 = (x & 0b0101)
print(bin(x2))
x2 = x2 << 1
print(bin(x2))
merge bits 
print(bin(x1|x2))
'''
