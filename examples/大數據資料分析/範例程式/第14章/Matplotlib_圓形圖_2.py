import csv
import matplotlib.pyplot as plt

city = []
population = []

#讀取檔案並將資料加入相對應的串列
with open('csvfile3.csv') as file:
    data = list(csv.reader(file))
    for record in data[1:]:
        city.append(record[0])
        population.append(record[1])

#各部門名稱
keys = city
#自訂各城市的顏色
colors = ['violet', 'yellow', 'skyblue', 'lightcoral', 'lightgreen', 'gold']
#突顯"New Taipei City"
explode = [0.1, 0, 0, 0.1, 0, 0]
#數據顯示格式
autopct = '%.1f%%'
#起始角度
startangle = 90

#繪出圓形圖
plt.pie(population, 
        labels=keys, 
        explode=explode, 
        colors=colors, 
        autopct=autopct, 
        startangle=startangle)
#強制使得圓形圖為圓形（否則將是橢圓形）
plt.axis('equal')
#圖表標題，字型大小為20
plt.title('Provincial Cities Population', size=20)
#顯示圖表
plt.show()