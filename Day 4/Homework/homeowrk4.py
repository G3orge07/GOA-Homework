
#  exercise 1 - make a user give us their name, their friends name, and print them together using concatination

print( "Please Enter 1) Your name  2) Your Friend's name")

your_name = input()
your_friends_name = input()

print(your_name + your_friends_name)



# exercise n2 - make a user give us their age and then print what age would they be in 10 years.

print("Please Enter Your Age")

your_age = input()

print (int(your_age) + 10)




# exercise n3 - make a user give us five numbers and then print the arithmetic average of those numbers

print("Please Enter 5 numbers")

number1 = input()
number2 = input()
number3 = input()
number4 = input()
number5 = input()

sum = int(number1)+int(number2)+int(number3)+int(number4)+int(number5)
arithmetic_average = sum/5

print(arithmetic_average)



#exercise n4

# Case-სენსიტიურობა გულისხმობს იმას, თუ როგორ აღიქვამს პროგრამირების ენა პატარა და დიდ ასოებს (uppercase, lowercase), 
# მაგალითად, Python არის Case-Sensitive, რაც იმას ნიშნავს, რომ ერთი და იგივე სიტყვები არ აღიქმება როგორც ერთი, თუ ერთი სიტყვა ან მასში ერთი ასოც კი დიდი ასოებითაა დაწერილი, ხოლო მეორე პატარებით.
# ცვლადი name, და ცვლადი "Name" ან "NAME" Python-ში ერთი არ არის. ზუსტად ესაა Case-Sensitivity


#snake case არის ერთ ცვლადში ორი ან მეტი სიტყვის დაწერის ერთ-ერთი ხერხი. snake case-ის მიხედვით, ცვლადში სიტყვებს შორის ქვედა-ტირე (underscore) უნდა დავწეროთ
#მაგალითად your_name (როგორც ამ ფაილში); shopping_cart; file_name etc.



#exercise n5 - make five errors and write the correct code by using comments, then describe what are bugs/debugging.


#1st error - a quotation mark is missing

name = "Giorgi

# name = "Giorgi"


#2nd error - a variable is printed before it's declared

print (name)
name = "Giorgi"

# name = "Giorgi"
# print (name)


#3rd error - a parenthesis is missing
age1 = 23
age2 = 25
age3 = 30

print (age1 + age2+ age3

# age1 = 23
# age2 = 25
# age3 = 30

# print (age1 + age2+ age3)



#4th error - the variable's first letter is in uppercase

Balance = 2457

print(balance)

# balance = 2457
# print(balance)



#5th error - the division operator's symbol is wrong

print ( 5 : 2)

# print( 5/2 )


#Bug/Debugging
# Bug არის იგივე რაც error, შეცდომა, რაც კოდის წერის დროს დავუშვით. კომპიუტერი პირველივე შეცდომაზე აჩერებს კოდის გაშვებას.
# Debugging კი არის ის რასაც სიტყვა გვეუბნება, ამ bug-ების გასწორება, კოდში დაშვებული შეცდომების ჩასწორება.
# python- ის შემთხვევაში ტერმინალი თვითონ გვეუბნება თყ რომელ ხაზზე და რა შეცდომა დავუშვით, რომ უფრო გაგვიმარტივდეს მათი აღმოფხვრა.



