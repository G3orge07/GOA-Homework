#Kata - Small enough? - Beginner

#https://www.codewars.com/kata/57cc981a58da9e302a000214/train/python

def small_enough(array, limit):
    result = True
    
    for num in array:
        if num > limit:
            result = False
    
    return result