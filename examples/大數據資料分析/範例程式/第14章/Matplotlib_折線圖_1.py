from matplotlib import pyplot as plt
import numpy as np

#12個月的銷售額
sale = np.array([22, 22, 17, 21, 22, 19, 21, 19, 20, 15, 24, 19])
#12個月的利潤
profit = np.array([12, 15, 11, 17, 11, 12, 11, 10, 16, 16, 13, 11])

x = np.arange(1, 13)
#以'b'(藍色)和'-o'(線和點)畫出第一條線，線粗度為2
plt.plot(x, sale, 'b-o', linewidth=2)
#以'r'(紅色)和'-o'(線和點)畫出第二條線，線粗度為2
plt.plot(x, profit, 'r-o', linewidth=2)
#設定x軸的範圍：從0到12、間隔1
plt.xticks(x)
#設定y軸的範圍：從0到24、間隔2
plt.yticks(np.arange(0, max(sale)+1, 2))
#設定x軸名稱，字型大小為16
plt.xlabel('Month', size=16)
#設定y軸名稱，字型大小為16
plt.ylabel('Million Dollars', size=16)
#設定圖的名稱，字型大小為16
plt.title('Sales and Profit in one year', size=20)
#顯示圖
plt.show()