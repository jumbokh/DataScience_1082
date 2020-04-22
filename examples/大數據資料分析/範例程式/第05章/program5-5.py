gcd = 1
n = 2
a = eval(input('Enter a number: '))
b = eval(input('Enter a number: '))
while n <= a and n <= b:
    if a % n == 0 and b % n == 0:
        gcd = n
    n += 1
print('GCD(%d, %d) = %d'%(a, b, gcd))