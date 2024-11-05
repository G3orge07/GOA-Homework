
#დაწერე ფუნქცია, რომელიც იღებს ორი რიცხვის მნიშვნელობას input() საშუალებით და ბეჭდავს მათ ჯამს.

def two_number_sum():
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    sum = num1 + num2
    print(f"The sum of those numbers are {sum}.")

two_number_sum()