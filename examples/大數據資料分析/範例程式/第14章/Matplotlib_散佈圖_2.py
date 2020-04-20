import numpy as np
import csv
import matplotlib.pyplot as plt

x = []
y = []

#讀取檔案資料並將資料加入x串列和y串列
with open('csvfile2.csv') as file:
    data = list(csv.reader(file))
    for record in data[1:]:
        x.append(eval(record[0]))
        y.append(eval(record[1]))

#繪出散佈圖，點大小為50，點樣式為正三角形，顏色為隨機介於0~1之間，透明度為0.7
plt.scatter(x, y, s=50, marker='o', c=np.random.rand(100), alpha=0.7)
#設定X軸名稱
plt.xlabel('x_value', size=14)
#設定Y軸名稱
plt.ylabel('y_value', size=14)
#設定X軸刻度為0到10
plt.xticks(np.arange(-80, 81, 10))
#設定Y軸刻度為0到100，間隔20
plt.yticks(np.arange(-300, 301, 40))
#設定圖表標題
plt.title('Scatter Chart', size=20)
#顯示圖
plt.show()