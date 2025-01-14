# Kata - How many double digits?
#https://www.codewars.com/kata/60fb2e158b940b00191e24fb/train/python

def number_of_duplicate_digits(ndigit):
    result = 0
    min = int('1' + (ndigit - 1) * '0')
    max = int(len(str(min)) * '9')
    
    for i in range( min, max+1):
        has_double_digits = False
        for n in range(len(str(i))-1):
            if str(i)[n] == str(i)[n+1]:
                has_double_digits = True
                break
        if has_double_digits:
            result +=1
            
    return result