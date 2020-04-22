import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(500, 50, 2000)
#以等差級數決定方盒的數量：40
bins = np.linspace(np.ceil(min(data)), np.floor(max(data)), 40)
#繪出直方圖，顏色為橘色，透明度為0.5
plt.hist(data, bins, color='red', alpha=0.5)
#設定Y軸刻度
plt.ylim([0, 160])
#設定X軸名稱
plt.xlabel('X-value', size=14)
#設定Y軸名稱
plt.ylabel('Y-value', size=14)
#設定圖標題
plt.title('Normal Distribution', size=20)
#顯示圖
plt.show()