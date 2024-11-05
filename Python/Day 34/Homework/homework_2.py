
#დაწერე ფუნქცია, რომელიც იღებს რიცხვს input()-ით და ბეჭდავს მის კვადრატს.

def square():
    number = int(input("Enter a number, so we can calculate its square: "))
    number_square = number * number
    print(f"The square of {number} is {number_square}!")

square()