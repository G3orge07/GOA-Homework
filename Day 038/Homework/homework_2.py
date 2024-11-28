#შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია შემდეგ კი ამ ფუნქციამ უნდა დააბრუნოს უდიდესი რიცხვი ამ სიიდან

numbers=[2,45,-78,240,100,33,999,456,2029,10]

def biggest_num(numbers_list):
    
    max_number = numbers_list[0]

    for i in range(len(numbers_list)):
        if max_number < numbers_list[i]:
            max_number = numbers_list[i]
        
    return max_number

print(biggest_num(numbers))