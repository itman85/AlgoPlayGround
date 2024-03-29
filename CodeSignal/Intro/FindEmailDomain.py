'''
An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.

Given a valid email address, find its domain part.

Example

For address = "prettyandsimple@example.com", the output should be
solution(address) = "example.com";
For address = "fully-qualified-domain@codesignal.com", the output should be
solution(address) = "codesignal.com".
'''


# Tip split, s[-1]: get last item

def solution(address):
    index = address.rindex('@')
    if index < 1 or index == len(address) - 1:
        return ""
    return address[index + 1:]


def solution1(a):
    return a[a.rfind("@") + 1:]  # make sure len > 0


def solution2(address):
    return address.split('@')[-1]


print(solution("fully-qualified-domain@codesignal.com"))
