
# Kata - Array.diff
#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    c = []
    for num in a:
        if num not in b:
            c.append(num)
            
    return c


# or

def array_diff(a, b):
    c = []
    
    for num in a:
        in_b = True
        
        for n in b:
            if num == n:
                in_b = False
                
        if in_b:
            c.append(num)
            
    return c