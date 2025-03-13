
# Kata - Is it a palindrome?


def is_palindrome(s):
    s_reverse = ''
    for i in range(1, len(s)+1 ):
        s_reverse += s[-i]
        
    return s_reverse.lower() == s.lower()