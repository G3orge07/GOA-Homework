
# Kata - Jaden Casing Strings

# https://www.codewars.com/kata/5390bac347d09b7da40006f6/solutions/python

def to_jaden_case(string):
    string_words = string.split(' ')
    
    for i in range(len(string_words)):
        string_words[i] = string_words[i].capitalize()
        
    return ' '.join(string_words)

