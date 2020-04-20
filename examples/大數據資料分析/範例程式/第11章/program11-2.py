import random
s2 = tuple([random.randint(1, 49) for i in range(1,100)])
print(s2)
lottoNums = 50*[0]
for i in range(len(s2)):
    k = s2[i]
    lottoNums[k] += 1

for j in range(1, len(lottoNums)):
    print('%d: %d'%(j, lottoNums[j]))