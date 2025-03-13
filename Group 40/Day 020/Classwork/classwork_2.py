# 1 დან 100 მდე დაბეჭდეთ ყოველი ლუწი რიცხვი და მიუწერეთ მათ რომ ლუწია, შემდეგ 1 და 100 მდე დაბეჭდეთ ყოველი კენტი რიცხვი და მიუწერეთ რომ კენტია, გამოიყენეთ მხოლოდ ლუპი

nums = []

for i in range(1, 101):
    nums.append(i)

for num in nums:
    if num % 2 == 0:
        print(str(num) + ' - Even')
    else:
        print(str(num) + ' - Odd')