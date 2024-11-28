#მომხმარებელს შეეკითხეთ სახელი შემდეგ შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ მომხმარებლის სახელს შემდეგ კი დააბრუნეთ მომხმარებლის სახელის პირველი ასო მერამდენეა ანბანში
name1= input("Enter your name: ")

letters= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def first_letter(name, alphabet):
    letter1 = name[0].upper()
    return alphabet.index(letter1)+1

        
print(first_letter(name1, letters))
