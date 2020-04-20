import numpy as np
import matplotlib.pyplot as plt

#馬拉松男性參賽者人數
male = [20, 48, 52, 31, 22]
#馬拉松女性參賽者人數
female = [19, 50, 44, 25, 20]

#年齡組合的數量
index = np.arange(len(male))
width = 0.35

fig, ax = plt.subplots()
#畫出男性參賽者的長條圖
rects1 = ax.bar(index, male, width=0.35, color='r')
#畫出女性參賽者的長條圖
rects2 = ax.bar(index + width, female, width, color='y')

#設定圖表名稱以及x軸、y軸名稱和標籤
ax.set_title('Quantity by group and gender', fontsize=18)
ax.set_xlabel('Age range', fontsize=14)
ax.set_ylabel('Quantity', fontsize=14)
ax.set_xticks(index + width / 2)
ax.set_xticklabels(['10~15', '16~20', '21~25', '25~30', '31~35'])
ax.set_yticks(np.arange(0, 51, 10))

#顏色註解
ax.legend((rects1[0], rects2[0]), ['Male', 'Female'])

plt.show()