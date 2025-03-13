# Kata - Find the smallest integer in the array

def find_smallest_int(arr):
    lowest_num = arr[0]

    for i in range(len(arr)):
        if lowest_num > arr[i]:
            lowest_num = arr[i]
        
    return lowest_num