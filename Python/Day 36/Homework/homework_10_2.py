
user_number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# prime_numbers =[]
# def check(num):
#     for a in range(len(num)):
#         if num[a] >= 2:
#             for i in range(2, num):
#                 if num[a] % i == 0:
#                     return "No numbers are prime numbers."
#                 else:
#                     prime_numbers.append(num[a])
#     return prime_numbers
# print(check(user_number_list))

prime_numbers=[]
not_prime_numbers=[]
def filter_prime(list)
    for i in range(len(list)):
        if list[i] <= 2:
            not_prime_numbers.append(list[i])
        else:
            for a in range(len(user_number_list)):
                