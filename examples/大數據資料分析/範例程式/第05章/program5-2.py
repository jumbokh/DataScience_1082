data = eval(input('Enter a number: '))
isPrime = True
divisor = 2
while divisor <= data / 2:
    if data % divisor == 0:
        isPrime = False
        break
    divisor += 1
if isPrime:
    print('%d is a prime number.'%(data))
else:
    print('%d is not a prime number.'%(data))