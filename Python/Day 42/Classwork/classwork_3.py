# Kata - String Repeat
#Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.


def repeat_str(repeat, string):
    new_string = ''
    for i in range(repeat):
        new_string += string
    return new_string