
#დაწერე ფუნქცია, რომელიც ამოწმებს, არის თუ არა რიცხვი ნულზე დიდი.

def more_than_zero_check(num):
    if num > 0:
        more_than_zero = True
    else:
        more_than_zero = False
    return more_than_zero

print(more_than_zero_check(-56))
print(more_than_zero_check(345))