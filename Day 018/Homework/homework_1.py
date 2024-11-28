# შექმენით ბანკის სისტემა სადაც იქნება ძალიან ბევრი პირობები და გამოიყენებთ if, elif და else -ს, გამოიყენებთ ასევე განვლილ მასალასაც


input('Enter Your Username: ')

print('Welcome To The Bank!')

balance = 500

print('Type:')
print('1. Check balance')
print('2. Add money')
print('3. Take money')
print('4. Exit')

choice = input()

if choice == '1':
    print('Balance - ₾' + str(balance))

elif choice =='2':
    add = int(input('Add money: ₾'))
    balance += add
    print('₾ ' + str(add) + ' added to your account.')

elif choice == '3':
    take = int(input('Take money: ₾'))
    if take > balance:
        print('Not enough money in your balance.')
    else:
        balance -= take
        print('₾ ' + str(take) + ' taken from your account.')

elif choice == '4':
    print('Logged out.')
    