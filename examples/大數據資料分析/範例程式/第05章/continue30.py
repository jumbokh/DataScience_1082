total = 0
i = 1
while i <= 100:
    if i % 5 == 0:
        i += 1
        continue
    else:
        total += i
        i += 1
print('total = %d'%(total))