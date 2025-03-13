
#დაწერე ფუნქცია, რომელიც იღებს სახელს input()-ით და ბეჭდავს ამ სახელის სიმბოლოების რაოდენობას.

def name_letters():
    name = input()
    letters = len(name)
    print(f"Did you know that there are {letters} letters in your name? You probably did.")

name_letters()