
#დაწერე ფუნქცია, რომელიც იღებს სიას და აბრუნებს მასში მხოლოდ მარტივ რიცხვებს.


#  1. ფუნქცია, რომელიც ამოწმებს მარიტივა თუ არა რიცხვი.
def prime_number(num):
    if num <2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True


# 2. ფუნქცია, იღებს სიას და აბრუნებს მასში მხოლოდ მარტივ რიცხვებს.
#PM - prime number

def list_PM_check(num1, num2, num3, num4, num5):
    numbers = [num1, num2, num3, num4, num5]
    prime_numbers = []
    
    for i in range(len(numbers)):
        if prime_number(i):
            prime_numbers.append(i)
    
    return prime_numbers


print(list_PM_check(1, 2, 3, 4, 5))