
#დაწერე ფუნქცია, რომელიც იღებს ორი რიცხვის მნიშვნელობას input() საშუალებით და ბეჭდავს მათ ჯამს.

def two_number_sum():
    num1 = int(input())
    num2 = int(input())
    sum = num1 + num2
    print(str(num1) + ' + ' + str(num2) + ' = '  + str(sum))

two_number_sum()
