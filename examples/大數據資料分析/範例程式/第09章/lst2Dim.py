import random
lst = []
rows = eval(input('How many rows: '))
columns = eval(input('How many columns: '))
for i in range(rows):
    lst.append([])
    for j in range(columns):
        num = random.randint(1, 49)
        lst[i].append(num)

for x in range(rows):
    for y in range(columns):
        print('%3d'%(lst[x][y]), end = ' ')
    print()