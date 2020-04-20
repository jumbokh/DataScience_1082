#Generating lotto number using set 
import random
set10 = set()
count = 1
while count <= 6:
    randNum = random.randint(1, 49)
    if randNum not in set10:
        set10.add(randNum)
        count += 1
      
print(set10)