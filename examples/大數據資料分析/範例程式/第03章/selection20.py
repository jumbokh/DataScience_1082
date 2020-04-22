a = eval(input('Enter a number1: '))
b = eval(input('Enter a number2: '))
if b != 0:
    c = a / b
    print('%.2f/%.2f = %.2f'%(a, b, c))
else:
    print('Divisor can\'t be zero')
print('Over')