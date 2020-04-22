total = 0
a = eval(input('Enter a number: '))
while True:
    total += a
    a = eval(input('Enter a number: '))
print('total = %d'%(total))