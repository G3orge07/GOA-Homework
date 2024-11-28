
#დაწერე ფუნქცია, რომელიც მიიღებს სიას და აბრუნებს მასში მყოფი ელემენტების რაოდენობას.


#function 1 - სიას იღებს არგუმენტის სახით
list1 =[1,2,3,4,5,6,7,8]

def list_len(list):
    return len(list)

print(list_len(list1))




#function 2 - მომხმარებელი ქმნის სიას

list2=[]
def list_length(List):
    print("Creating a list...")
    List.append(input("Enter the 1st item: "))

    continue_adding = True
    while continue_adding == True:
        List.append(input("Enter the next item: "))
        choice = input(("Would you like to keep going? Type + if yes, type - if not: "))
        if choice == "+":
            continue_adding = True
        else:
            continue_adding = False

    return len(List)


print(list_length(list2))

