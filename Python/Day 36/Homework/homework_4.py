
#დაწერე ფუნქცია, რომელიც მიიღებს სიას და აბრუნებს მასში მყოფი ელემენტების რაოდენობას.

List = []

def list_length():
    continue_adding = True
    print("You are going to create a list as long as you like and then we are going to calculate the length of it!")
    List.append(input("Enter the 1st item: "))

    while continue_adding == True:
        List.append(input("Enter the next item: "))
        choice = input(("Would you like to keep going? Type + if yes, type - if not: "))
        if choice == "+":
            continue_adding = True
        else:
            continue_adding = False

    return List


print(list_length())

print("The length of your list is "  + str(len(List)))
