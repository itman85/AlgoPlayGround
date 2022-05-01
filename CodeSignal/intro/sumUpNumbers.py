'''
CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
solution(inputString) = 14.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
0 ≤ inputString.length ≤ 105.

[output] integer
'''
import re


def solution(inputString):
    return sum([int(i) for i in re.split('[^0-9]', inputString) if
                i.isdigit()])  # split include empty string so need to check isdigit


def solution1(inputString):
    l = re.findall(r"\d+", inputString)  # return list number only
    return sum([int(i) for i in l])


# lst = re.split('[^0-9]',inputString)
# print(lst)

# Tips: split numbers in string by regex use '[^0-9]' or '\d+'

print(solution("there are some (12) digits 5566 in this 770 string 239"))
