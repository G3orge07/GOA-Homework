# Kata - Remove String Spaces

def no_space(x):
    list = x.split(" ")
    split_x = ''
    for i in list:
        split_x += i
    return split_x