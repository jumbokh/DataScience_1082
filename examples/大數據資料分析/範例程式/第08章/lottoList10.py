import random

lotto = []
lotto.append(random.randint(1, 49))

for m in range(1, 6):
    n = 0
    while n < m :
        temp = random.randint(1, 49)
        if(temp == lotto[n]):
            n = 0
        else:
            n += 1
    lotto.append(temp)
           
print("The lottery numbers are: ")
for i in lotto:
    print('%4d'%(i), end = '  ')
print()