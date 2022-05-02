'''
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
solution(time) = true;
For time = "25:51", the output should be
solution(time) = false;
For time = "02:76", the output should be
solution(time) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string time

A string representing time in HH:MM format. It is guaranteed that the first two characters, as well as the last two characters, are digits.

[output] boolean

true if the given representation is correct, false otherwise.
'''
import re


def solution(time):
    return re.match('^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$', time) is not None


def solution2(time):
    h, m = map(int, time.split(":"))
    return 0 <= h < 24 and 0 <= m < 60


print(solution("13:58"))
