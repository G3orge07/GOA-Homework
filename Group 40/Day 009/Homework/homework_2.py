
#  შექმენით დროში მოგზაურობის პროგრამა, რომელიც მომხმარებელს შეეკითხება მის ამჟამინდელ ასაკს, ამჟამინდელ წელს, რამდენი წლით სურს დროში მოგზაურობა, შემდეგ კი პროგრამა დაბეჭდავს დროში მოგზაურობის შემდეგ რომელი წელი იქნება და რამდენი წლის იქნება მომხმარებელი დროში მოგზაურობის შემდეგ

print('Welcome to the time machine!')

age = int(input('How old are you right now? '))
year = int(input('What year is it? '))

travel = int(input('Would you like to travel to the    1. Past     2.Future   '))

if travel ==1:
    travel_year = int(input('How many years are you traveling in the past?'))

    if travel_year > age:
        print('Traveling...')
        print('It is the year ' + str(year - travel_year) + ', you are not born yet.')

    elif travel_year == age:
        print('Traveling...')
        print('It is the year ' + str(year - travel_year) + ', you will be born this year.')

    else:
        print('Traveling...')
        print('It is the year ' + str(year - travel_year) + ', you are ' + str(age - travel_year) + ' years old.')


elif travel == 2:
    travel_year = int(input('How many years are you traveling into the future?'))

    print('Traveling...')
    print('It is the year ' + str(year + travel_year) + ', you are ' + str(age + travel_year) + ' years old.')