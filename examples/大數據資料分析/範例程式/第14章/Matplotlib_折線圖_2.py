import csv
import numpy as np
from matplotlib import pyplot as plt

x_labels = [] #儲存x軸標籤
#以讀檔模式開啟csvfile1.csv檔案
with open('csvfile1.csv', 'r') as csvfile:
    #利用csv.reader解析檔案格式，並將結果轉換成串列
    rows = list(csv.reader(csvfile, delimiter=','))
    #取得第一列第一個元素往後所有元素
    categories = rows[0][1:]
    #建立用以存取每個類別各季的利潤
    categories_profit = [[0] * (len(rows)-1) for _ in range(len(categories))]
    #對從第二列開始每一列，
#取第一個元素坐位x軸標籤
#取其餘元素作為資料
    #i代表季節，j代表分類
    for i in range(1, len(rows)):
        x_labels.append(rows[i][0])
        for j in range(len(categories)):
            categories_profit[j][i-1] = eval(rows[i][j+1])

lines = []
x = np.arange(1, 5)
#以'-o'(線和點)畫出三條線，線粗度為2
for i in range(len(categories)):
    #每畫一條線則記錄下來，以便作顏色註解
    line, = plt.plot(x, categories_profit[i], '-o', linewidth=2)
    lines.append(line)
    
#設定x軸的範圍：從1到4、間隔1
plt.xticks(np.arange(1, 5, 1), x_labels)
#設定y軸的範圍：從0到250、間隔50
plt.yticks(np.arange(0, 251, 50))
#設定x軸名稱，字型大小為16
plt.xlabel('Season', size=16)
#設定y軸名稱，字型大小為16
plt.ylabel('Thousand Dollars', size=16)
#設定圖的名稱，字型大小為16
plt.title('Profit earned in one year', size=20)
#顏色註解
plt.legend(lines, categories)
#顯示圖
plt.show()