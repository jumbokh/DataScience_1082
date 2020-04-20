total = 0
a = eval(input('Enter a number: '))
while True:
    if a != -999:
        total += a
        a = eval(input('Enter a number: '))
    else:
        break
print('total = %d'%(total))