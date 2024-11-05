
#დაწერე ფუნქცია, რომელიც მიიღებს რიცხვების სიას და გამოიყვანს თითოეულს კვადრატში აყვანილს.

def square(num1, num2, num3, num4, num5):
    num1_sq = num1**2
    num2_sq = num2**2
    num3_sq = num3**2
    num4_sq = num4**2
    num5_sq = num5**2
    nums_squared = [num1_sq, num2_sq, num3_sq, num4_sq, num5_sq]
    return nums_squared

print(square(3, 12, 50, 22, 147))
