count = 0
for i in range(2, 101):
    divisor = 2
    isPrime = True
    while divisor <= i / 2:
        if i % divisor == 0:
            isPrime = False
            break
        divisor += 1
    if isPrime:
        count += 1
        if count % 10 != 0:
            print('%3d'%(i), end = ' ')
        else:
            print('%3d'%(i))