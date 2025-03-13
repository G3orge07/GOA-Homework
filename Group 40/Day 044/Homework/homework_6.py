# Kata - Counting sheep...

def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s:
            count += 1
    return count