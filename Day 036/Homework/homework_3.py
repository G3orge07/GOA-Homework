
#დაწერე ფუნქცია, რომელიც ამოწმებს, არის თუ არა რიცხვი ნულზე დიდი.

def more_than_zero(num):
    if num > 0:
        return True
    if num == 0:
        return 0
    else:
        return False

print(more_than_zero(-56))
print(more_than_zero(345))
print(more_than_zero(0))