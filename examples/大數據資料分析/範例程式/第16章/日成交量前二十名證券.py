import pandas as pd   #載入pandas套件，縮寫為pd
import requests as rq   #載入requests套件，縮寫為rq

#“日成交量前二十名證券”資料來源
url = 'http://www.twse.com.tw/exchangeReport/MI_INDEX20?response=json&date=&_=1513501982216'
r = rq.get(url)   #發出 html get 請求

#將請求結果轉換成json格式並顯示查看轉換結果
json_data = r.json()

#將json資料轉換成 pandas DataFrame 型態 （參數1：資料內容，型態為list；參數columns：指定欄位名稱，型態為list）
df = pd.DataFrame(json_data['data'], columns=json_data['fields'])
print(df)

#顯示'漲跌(+/-)'欄位
print(df['漲跌(+/-)'])

#處理'漲跌(+/-)'欄位：去掉'+'或'-'以外的字元
for i in range(len(df['漲跌(+/-)'])):
      #檢查該筆資料的'漲跌(+/-)'欄位是否為空
    if df['漲跌(+/-)'][i] == '':
          #若是，則跳過這筆資料
        continue
    else:   #否則，進行處理
        #抓出該筆資料'+'或'-'的索引位置
        index_of_target = df['漲跌(+/-)'][i].index('>') + 1
        #取得'+'或'-'單一字元
        target = df['漲跌(+/-)'][i][index_of_target]
        #以取得的字元將整比資料替換掉
        df['漲跌(+/-)'][i] = target
print(df)   #顯示處理後結果