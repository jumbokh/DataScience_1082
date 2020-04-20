def average(a, b):
    total = a + b
    aver = total / 2
    return total, aver

def main():
    x, y = eval(input('Enter 2 numbers: '))
    tot2, aver2 = average(x, y)
    print('total = %d, average = %.2f'%(tot2, aver2))

main()