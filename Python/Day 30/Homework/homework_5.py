
# 5) შექმენით სია რომელშიც იქნება ხილის სახელები შეაპარეთ რამდენიმე განსხვავებული სახელი რომელიც ხილი არარის შემდეგ კი ხელით ამოშალეთ ამ სიიდან ისეთი ელემენტები რომლებიც არ არის ხილი

fruit = ['Apple', 'Banana', 'Cheeseburger','Orange', 'Strawberry', 'Cherry', 'Pizza', 'Carrot', 'Mandarin']

not_fruit = ['Pizza', 'Cheeseburger', 'Carrot']

for i in not_fruit:
    fruit.remove(i)

print(fruit)