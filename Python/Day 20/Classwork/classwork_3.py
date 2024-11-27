# 1-დან 100-მდე დაითვალეთ ხუთის ჯერადი რიცხვების ჯამი გამოიყენეთ if, else გამოგადგებათ % ნიშანი

nums = []

for i in range(1, 101):
    nums.append(i)

count = 0

for num in nums:
    if num % 5 ==0:
        count += 1

print(count)

