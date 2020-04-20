import pandas as pd
import numpy as np

df = pd.read_csv('file1.csv')

#改變索引為從1開始並顯示結果
df = df.set_index(np.arange(1, len(df)+1))
print(df)

#顯示前兩筆記錄
print('\n前兩筆記錄：\n%s' % df[:2])
#獲取"白醋"的進貨記錄
print('\n"白醋"的進貨記錄：\n%s' % df[df['商品名稱'] == '白醋'])

#計算各單位商品數量
print("\n各單位商品數量：\n%s" % df.groupby('單位')['商品名稱'].count())
#根據進貨日期從小到大排序
print('\n根據進貨日期從小到大排序：\n%s' % df.sort_values(by='進貨日期'))