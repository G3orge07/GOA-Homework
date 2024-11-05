
#დაწერე ფუნქცია, რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი.


#version 1

def odd_or_even():
    num = int(input("Type in a number: "))
    if num %2 == 0:
        return "The number is even"
    else:
        return "The number is odd"

print(odd_or_even())



#version 
# 2
def ODD_OR_EVEN(NUM):
    if NUM %2 == 0:
        return "The number is even"
    else:
        return "The number is odd"

print(ODD_OR_EVEN(1089))