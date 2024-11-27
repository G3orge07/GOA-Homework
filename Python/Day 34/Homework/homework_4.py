
#დაწერე ფუნქცია, რომელიც input()-ით იღებს ორ რიცხვს და ბეჭდავს, რომელია დიდი.

def comparison():
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    if num1 > num2:
        print(f"{num1} is bigger than {num2}.")
    else:
        print(f"{num2} is bigger than {num1}.")

comparison()

