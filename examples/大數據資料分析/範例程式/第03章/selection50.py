year = eval(input('Enter a year: '))
con1 = year % 400 == 0
con2 = year % 4 == 0
con3 = year % 100 != 0
if con1 or (con2 and con3):
    print('%d is a leap year.'%(year))
else:
    print('%d is a common year.'%(year))