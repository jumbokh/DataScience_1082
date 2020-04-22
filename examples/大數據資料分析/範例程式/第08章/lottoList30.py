#using list and not in to solve duplicate number
import random
lotto = []
count = 1

while count <= 6:
    randNum = random.randint(1, 49)
    if randNum not in lotto:
        lotto.append(randNum)
        count += 1

lotto.sort()
for i in lotto:
    print(i, end = '  ')
print()