
#დაწერე ფუნქცია, რომელიც იღებს რიცხვს და ამოწმებს, არის თუ არა ის მარტივი რიცხვი.

def prime_number(num):
    if num <2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True
    
print(prime_number(37))
print(prime_number(92))