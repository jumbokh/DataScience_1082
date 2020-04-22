import pandas as pd   #載入pandas套件，縮寫為pd
import json   #載入json套件以讀取json格式的資料

#以單一個檔案為例
path = 'C:\\Data Science with Python\\Data\\201709\\智慧財產法院民事\\IPCV,104,民專上,13,20170921,5.json'
#開啟檔案
with open(path, 'r', encoding='utf-8') as file:   #讀取json資料
    data = json.load(file)

a = {key: value for key, value in data.items()}  #將資料轉換為詞典
b = [x for x in range(1, len(a)+1)]   #定義資料索引
df = pd.DataFrame(a, index=b)   #將資料轉換成DataFrame
print(df)