
# Kata - Grasshopper - Summation

def summation(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum


#or

def summation(num):
    return sum(range(1, num+1))