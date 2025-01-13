
# Kata - Find The Parity Outlier

#https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(integers):
    even_count = 0
    
    for int in integers:
        if int %2 == 0:
            even_count += 1
            
    if even_count == 1:
        for num in integers:
            if num %2 == 0:
                return num
    else:
        for num in integers:
            if num % 2 != 0:
                return num