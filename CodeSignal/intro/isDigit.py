'''
Determine if the given character is a digit or not.

Example

For symbol = '0', the output should be
solution(symbol) = true;
For symbol = '-', the output should be
solution(symbol) = false.
'''

def solution(symbol):
    return ord('0') <= ord(symbol) <= ord('9')

def solution1(symbol):
    return symbol.isdigit()