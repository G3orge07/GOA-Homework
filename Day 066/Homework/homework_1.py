# Kata -Nickname Generator

#https://www.codewars.com/kata/593b1909e68ff627c9000186/train/python

def nickname_generator(name):
    if len(name) >= 4:
        if name[2] in ['a', 'e', 'i', 'o', 'u']:
            return name[0:4]
        else:
            return name[0:3]
    else:
        return "Error: Name too short"
    

print('3agh5gggR894Ghf8474ghf'.upper())