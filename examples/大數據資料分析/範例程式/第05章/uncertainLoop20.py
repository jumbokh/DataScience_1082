total = 0
a = eval(input('Enter a number: '))
while a != -999:
    total += a
    a = eval(input('Enter a number: '))
print('total = %d'%(total))