import random
print('Part 1')
for i in range(1, 7):
    lotto = random.randint(1, 38)
    print('%4d'%(lotto), end = '')

print('\nPart 2')
lotto2 = random.randint(1, 8)
print('%4d'%(lotto2))