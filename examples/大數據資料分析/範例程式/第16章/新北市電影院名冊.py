import requests as rq   #載入requests套件，縮寫為rq
import csv   #載入csv套件，以處理csv格式
import pandas as pd   #載入pandas套件，縮寫為pd

#新北市電影院名冊
url = \
'http://data.ntpc.gov.tw/od/data/api/61C99F42-8A90-4ADC-9C40-BA9E0EA097AA?$format=csv'
r = rq.request('GET', url)   #對url發出get請求

data = list(csv.reader(r.text.split('\n'), delimiter = ',', quotechar='"'))  
#將csv格式的字串轉換成二維串列

df = pd.DataFrame(data[1:len(data)-1], columns=['名稱','地址','電話號碼','廳數'])
#將資料集串列轉換成Data Frame
df.index += 1   #資料順序從1開始
print(df)