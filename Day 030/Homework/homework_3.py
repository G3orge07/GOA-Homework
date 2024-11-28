# 3) შექმენით თავდაპირველად ცარიელი სია მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი 1-დან ამ რიცხვამდე დაამატეთ ყველა რიცხვი სიაში გამოიყენეთ for loop და append

num_list = []

num = int(input("Enter a number: "))

for i in range(1, num+1):
    num_list.append(i)

print(num_list)