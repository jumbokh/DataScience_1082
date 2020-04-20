import pandas as pd
#商品名稱
products = ['iPhone', 'Samsung', 'Sony', 'Huawei', 'HTC', 'Oppo']
#存貨量
inventory = [1000, 1200, 1300, 800, 700, 850]
#建立詞典
data = {'商品名稱': products, '存貨': inventory}
#建立DataFrame，以data的keys作為欄位名稱
df = pd.DataFrame(data, columns=data.keys())

#將iPhone的存貨加50
df.loc[0, '存貨'] += 50
#輸出存貨最多的商品
print('存貨最多的商品： \n%s' % df[df['存貨'] == df['存貨'].max()])
#將資料根據存貨量從大到小排序
print('\n根據存貨量從大到小排序： \n%s' % df.sort_values(by='存貨', ascending=False))
#輸出存貨量少於1000的商品
print('\n存貨量少於1000的商品： \n%s' % df[df['存貨'] < 1000])