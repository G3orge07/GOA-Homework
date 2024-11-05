#შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია შემდეგ კი ფუნქციამ უნდა დააბრუნოს უმცირესი რიცხვი ამ სიიდან

def lowest(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    numbers=[num1, num2, num3, num4, num5, num6, num7,num8, num9, num10]
    lowest_num = numbers[0]

    for i in range(len(numbers)):
        if lowest_num > numbers[i]:
            lowest_num = numbers[i]
        
    return lowest_num

print(lowest(2,45,-78,240,100,33,999,456,2029,10))