for i in range(1, 51):
    factor = 1
    print('%2d! = '%(i), end = '')
    for j in range(1, i+1):
        factor = factor * j
    print(factor)