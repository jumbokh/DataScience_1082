import matplotlib.pyplot as plt

#A公司各部門及其員工數量
companyA = {'Personnel Department': 8,   #人事部門
            'Accounting Department': 5,  #會計部門
            'Design Department': 10,     #設計部門
            'Marketing Department': 12,  #行銷部門
            'Purchasing Department': 5}  #採購部門
#B公司各部門及其員工數量
companyB = {'Personnel Department': 10,  #人事部門
            'Accounting Department': 8,  #會計部門
            'Design Department': 20,     #設計部門
            'Marketing Department': 18,  #行銷部門
            'Purchasing Department': 12} #採購部門

#A公司各部門員工數量
companyA_values = companyA.values()
#B公司各部門員工數量
companyB_values = companyB.values()
#各部門名稱
keys = companyA.keys()
#各部門顏色
colors = ['violet', 'yellow', 'skyblue', 'lightcoral', 'lightgreen']
#突顯"行銷部門"
explode = [0, 0, 0, 0.1, 0]
#數據顯示格式
autopct = '%.1f%%'
#起始角度
startangle = 90

#繪出A公司的圓形圖
fig1, ax1 = plt.subplots()
ax1.pie(companyA_values, 
        labels=keys, 
        explode=explode, 
        colors=colors, 
        autopct=autopct, 
        startangle=startangle)
#強制使得圓形圖為圓形（否則將是橢圓形）
ax1.axis('equal')
#圖表標題為"Company A"，字型大小為20
ax1.set_title('Company A', size=20)

#繪出B公司的圓形圖
fig2, ax2 = plt.subplots()
ax2.pie(companyB_values, 
        labels=keys, 
        explode=explode, 
        colors=colors, 
        autopct=autopct, 
        startangle=startangle)
#強制使得圓形圖為圓形（否則將是橢圓形）
ax2.axis('equal')
#圖表標題為"Company B"，字型大小為20
ax2.set_title('Company B', size=20)

#顯示圖表
plt.show()