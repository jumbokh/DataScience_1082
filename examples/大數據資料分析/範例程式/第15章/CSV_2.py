import csv
import random

lottos = []
#產生12組大樂透號碼
for i in range(12):
    lottos.append(sorted(random.sample(range(1, 50), 6)))

#以寫入模式開啟lottos.csv
with open('lottos.csv', 'w', newline='') as file:
    writer = csv.writer(file) #建立csv的寫入器
    writer.writerows(lottos) #寫入12組大樂透號碼