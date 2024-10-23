
#დაწერეთ ფუნქცია რომელიც მომხმარებლისგან იღებს რიცხვს და თუ რიცხვი 1-დან 10-მდეა დაბეჭდავს თუარა დაუბეჭდავს "არასწორი რიცხვი"

def number_till_10():
    number = int(input("Please enter a number from 1 to 10: "))
    if number >= 1 and number <= 10:
        print(f"Thank you! You chose {number}")
    else:
        print("Wrong Number!")

number_till_10()




