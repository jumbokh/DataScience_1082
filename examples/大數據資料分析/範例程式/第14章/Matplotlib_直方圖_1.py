import numpy as np
from matplotlib import pyplot as plt

#100個學生的分數
data = [73, 71, 34, 85, 80, 100, 57, 78, 88, 98, 
        46, 34, 74, 86, 41, 54, 80, 40, 71, 46, 
        43, 51, 58, 61, 71, 70, 65, 39, 28, 62, 
        49, 89, 73, 38, 41, 51, 45, 64, 51, 34, 
        42, 58, 67, 56, 71, 45, 32, 42, 59, 98, 
        33, 64, 55, 67, 50, 45, 64, 63, 85, 39, 
        48, 62, 34, 67, 100, 58, 68, 34, 38, 70, 
        64, 74, 62, 73, 45, 17, 68, 26, 69, 56, 
        76, 59, 45, 95, 78, 77, 70, 59, 91, 79, 
        53, 78, 61, 84, 56, 96, 68, 64, 46, 70]
data = np.array(data) # 將分數串列轉換為np陣列
#以等差級數決定方盒的數量，為20
bins = np.linspace(np.ceil(min(data)), np.floor(max(data)), 20)
#繪出直方圖，顏色為橘色，透明度為0.5
plt.hist(data, bins, color='orange', alpha=0.5)
#設定X軸刻度
plt.xlim([0, 100])
#設定X軸名稱
plt.xlabel('Score', size=14)
#設定Y軸名稱
plt.ylabel('Quantity', size=14)
#設定圖標題
plt.title('Student Scores Distribution', size=20)
#顯示圖
plt.show()