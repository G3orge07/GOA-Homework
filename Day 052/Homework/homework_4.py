
# Kata - Shortest Word

#https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python


def find_short(s):
    shortest = len(s.split(' ')[0])
    
    for word in s.split(' '):
        if len(word) < shortest:
            shortest = len(word)
    
    return shortest