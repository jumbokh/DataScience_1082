year = eval(input('Enter your birthday year: '))
print('Your zodic is ', end = '')
zodic = year % 12
if zodic == 0:
    print('Monkey')
elif zodic == 1:
    print('Rooster')
elif zodic == 2:
    print('Dog')
elif zodic == 3:
    print('Pig')
elif zodic == 4:
    print('Rat')
elif zodic == 5:
    print('Ox')
elif zodic == 6:
    print('Tiger')
elif zodic == 7:
    print('Rabbit')
elif zodic == 8:
    print('Dragon')
elif zodic == 9:
    print('Snake')
elif zodic == 10:
    print('Horse')
else:
    print('Sheep')