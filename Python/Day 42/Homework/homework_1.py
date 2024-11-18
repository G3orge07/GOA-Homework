# Kata - Reversed Strings
# Complete the solution so that it reverses the string passed into it.


def solution(string):
    str_reverse = ''
    for i in string:
        str_reverse = i + str_reverse
    return str_reverse