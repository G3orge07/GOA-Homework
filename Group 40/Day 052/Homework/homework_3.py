
# Kata - Highest and Lowest

#https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

def high_and_low(numbers):
    numbers_list = numbers.split(' ')
    integers_list = []
    
    for i in numbers_list:
        integers_list.append(int(i))
    
    return str(max(integers_list)) + ' ' + str(min(integers_list))