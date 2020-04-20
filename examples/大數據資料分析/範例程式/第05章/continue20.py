total = 0
i = 1
while i <= 100:
    if i % 5 == 0:
        continue
    else:
        i += 1
        total += i
print('total = %d'%(total))