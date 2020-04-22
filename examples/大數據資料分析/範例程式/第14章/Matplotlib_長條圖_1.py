from matplotlib import pyplot as plt
import numpy as np

#學生分數
scores = [84, 83, 23, 63, 45, 43, 72, 65, 60, 73, 
    34, 26, 59, 20, 31, 63, 45, 79, 98, 35, 
    61, 76, 20, 90, 30, 45, 44, 92, 53, 93, 
    67, 33, 38, 24, 45, 46, 39, 49, 56, 75, 
    47, 72, 60, 40, 91, 69, 96, 49, 25, 35, 
    64, 20, 43, 65, 72, 78, 28, 53, 31, 100, 
    41, 65, 35, 51, 40, 37, 79, 69, 54, 49]

#range_count[0]: range0~19
#range_count[1]: range20~39
#range_count[2]: range40~59
#range_count[3]: range60~79
#range_count[4]: range80~100
#以0初始化計數串列
range_count = [0] * 5

#計數過程
for score in scores:
    if score < 20:
        range_count[0] += 1
    elif score < 40:
        range_count[1] += 1
    elif score < 60:
        range_count[2] += 1
    elif score < 80:
        range_count[3] += 1
    else:
        range_count[4] += 1

#y軸標籤
index = np.arange(0, 25, 5)
#x軸標籤
labels = ['0~19', '20~39', '40~59', '60~79', '80~100']
#畫出長條圖
plt.bar(index, range_count, width=2)
#設定x軸名稱
plt.xlabel('Range', fontsize=14)
#設定y軸名稱
plt.ylabel('Quantity', fontsize=14)
#設定x軸標籤
plt.xticks(index, labels)
#設定y軸標籤
plt.yticks(index)
#設定圖名稱
plt.title('Score ranges count', fontsize=20)
#顯示圖
plt.show()