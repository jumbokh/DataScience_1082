import numpy as np
import matplotlib.pyplot as plt

#隨機產生50個介於0~10之間的浮點數
x = np.random.rand(50) * 10
#隨機產生50個範圍1~100的整數
y = np.random.randint(1, 101, 50)

#繪出散佈圖，點大小為80，點樣式為上三角形
#顏色為隨機介於0~1之間，透明度為0.7
plt.scatter(x, y, s=80, marker='^', c=np.random.rand(50), alpha=0.7)
#設定X軸名稱
plt.xlabel('x_value', size=14)
#設定Y軸名稱
plt.ylabel('y_value', size=14)
#設定X軸刻度為0到10
plt.xticks(np.arange(11))
#設定Y軸刻度為0到100，間隔20
plt.yticks(np.arange(0, 101, 20))
#設定圖表標題
plt.title('Scatter chart', size=20)
#顯示圖
plt.show()