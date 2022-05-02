'''
You are given a string. Remove its first and last characters until the string is empty or the first and the last characters are not equal. Output the resulting string.

Example

For inputString = "abacaba", the output should be
solution(inputString) = "".

Explanation: "bacab" -> "aca" -> "c" -> "".

For inputString = "12133221", the output should be
solution(inputString) = "1332".
'''

# Tip  inputString[1:-1:] : substring from index 1 to len -1 with step = 1
def solution(inputString):
    while len(inputString) != 0 and inputString[0] == inputString[-1]:
        inputString = inputString[1:-1:]
    return inputString

print(solution("12133221"))
