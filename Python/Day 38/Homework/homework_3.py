#შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია შემდეგ კი ფუნქციამ უნდა დააბრუნოს უმცირესი რიცხვი ამ სიიდან

numbers=[2,45,-78,240,100,33,999,456,2029,10]

def lowest(number_list):

    lowest_num = number_list[0]

    for i in range(len(numbers)):
        if lowest_num > number_list[i]:
            lowest_num = number_list[i]
        
    return lowest_num

print(lowest(numbers))
