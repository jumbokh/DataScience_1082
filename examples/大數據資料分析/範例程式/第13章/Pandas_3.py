import pandas as pd
#建立名單--學生名字
names = ['Cathy', 'Daisy', 'Bonnie', 'Vicky', 'Mary']
#建立名單--學生分數
scores = [84, 98, 92, 80, 75]
#建立字典
data = {'Name': names, 'Score': scores}

#建立pandas的DataFrame資料結構
df = pd.DataFrame(data)
print('原始資料：')
print(df)
print()

#將資料根據名字從小到大排序
df = df.sort_values(by='Name')
print('將資料根據名字從小到大排序：')
print(df)
print()

#將資料根據分數從大到小排序
df = df.sort_values(by='Score', ascending=False)
print('將資料根據分數從大到小排序：')
print(df)
print()

#列出分數高於90分的學生
greater90 = df[df['Score'] > 90]
print('列出分數高於90分的學生：')
print(greater90)