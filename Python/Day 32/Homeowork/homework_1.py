
# 1) შექმენით რიცხვებით სავსე სია, შემდეგ დაწერეთ კოდი რომელიც დაბეჭდავს ამ სიიდან ყველაზე უდიდეს რიცხვს გამოგადგებათ for loop ი კარგად დაფიქრდით და გაიაზრეთ

number_list = [4, -45, 120, 78, 89, 407, 878, 23, 0, -55, 10]

max_number = number_list[0]


for i in range(len(number_list)):
    if max_number < number_list[i] :
        max_number = number_list[i]



print(max_number)
