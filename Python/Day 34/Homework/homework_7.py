
#შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და დააბრუნებს True, თუ ის ლუწია  და False, თუ არა.

def even_or_odd():
    number = int(input("Enter a number. If the number is even, it will show True, and if it's odd, it will show False: "))
    if number % 2 == 0:
        print(True)
    else:
        print(False)

even_or_odd()

