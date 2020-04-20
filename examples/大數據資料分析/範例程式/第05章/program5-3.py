for i in range(2, 101):
    divisor = 2
    isPrime = True
    while divisor <= i / 2:
        if i % divisor == 0:
            isPrime = False
            break
        divisor += 1
    if isPrime:
        print('%3d'%(i), end = ' ')