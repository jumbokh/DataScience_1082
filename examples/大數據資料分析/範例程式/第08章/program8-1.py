import random 
data = []
total = 0
for i in range(10):
    data.append(random.randint(1, 10))
    total += data[i]
print(data)
print('total = %d'%(total))