# 1) შექმენით სია რომელშიც იქნება მინიმუმ 10 სახელი შემდეგ ამ სიიდან ამოშალეთ ისეთი სახელები რომლის სიგრძეც იქნება 10ზე მეტი და დააბრუნეთ გაფილტრული სია გამოიყენეთ for loop და ნასწავლი ფუნქციები

name_list = ["Giorgi", "Levani", "Aleqsandre", "Mariam", "Nikoloz", "Elene", "Konstantine", "Luka", "Lasha-Giorgi", "Erekle"]

filt_name_list = []

for name in name_list:
    if len(name) < 10:
        filt_name_list.append(name)

print(filt_name_list)