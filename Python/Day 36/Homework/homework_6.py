
#დაწერე ფუნქცია, რომელიც მიიღებს რიცხვების სიას და გამოიყვანს თითოეულს კვადრატში აყვანილს.

def square(nums):
    nums_sq = []

    for num in nums:
        nums_sq.append(num**2)

    return nums_sq

print(square( [3, 12, 50, 22, 147] ))
