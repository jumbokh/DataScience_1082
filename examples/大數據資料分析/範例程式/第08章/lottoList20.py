#using list to solve duplicate number
import random
lotto = []
checkNum = []
count = 0

for i in range(50):
    checkNum.append(0)

while count <= 6:
    randNum = random.randint(1, 49)
    if checkNum[randNum] == 0:
        lotto.append(randNum)
        count += 1
        checkNum[randNum] = 1

lotto.sort()
for i in lotto:
    print('%3d'%(i), end = ' ')
print()