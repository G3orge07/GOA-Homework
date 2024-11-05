#შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია შემდეგ კი ამ ფუნქციამ უნდა დააბრუნოს უდიდესი რიცხვი ამ სიიდან


def biggest_num(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    numbers=[num1, num2, num3, num4, num5, num6, num7,num8, num9, num10]
    max_number = numbers[0]

    for i in range(len(numbers)):
        if max_number < numbers[i]:
            max_number = numbers[i]
        
    return max_number

print(biggest_num(2,45,-78,240,100,33,999,456,2029,10))