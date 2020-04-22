import pandas as pd
import numpy as np

data = {
        "水果名稱" : ['蘋果', '香蕉', '芭樂', '榴蓮', '草莓'],
        "存貨" : [22, 15, 33, 0, 36],
        "單位" : ['箱', '把' , '箱', '箱', '盒']
       }

df = pd.DataFrame(data, columns=data.keys(), 
                  index=np.arange(1, len(data['水果名稱'])+1))
print('原始資料：\n', df)
print()

#根據庫存量從大到小排序
df = df.sort_values(by='存貨', ascending=False)
print('根據庫存量排序後結果：\n', df)
print()

#單位為箱且庫存<=20的水果資料
print('單位為箱的水果資料：\n', df[(df['單位']=='箱') & (df['存貨']<=20)])