import requests as rq   #載入requests套件，縮寫為rq
import pandas as pd   #載入pandas套件，縮寫為pd

#載入ElementTree套件，縮寫為ET
from xml.etree import ElementTree as ET

#每月新北市A1類道路交通事故－肇事時間別
url = 'http://data.ntpc.gov.tw/od/data/api/7D58F2F5-E8E1-4D15-959F-26A16C8384AF?$format=xml'
r = rq.request('GET', url)   #發出GET請求

#將得到的內容（XML格式）轉換成ElementTree
data = ET.fromstring(r.content)

lst = []   #用以存放所有資料的串列
for i in data.iter('row'):   #針對每一筆'row'標籤
    record = []   #用以存放單筆資料的串列
    for j in i.iter():   #針對一個'row'中的每一個標籤
        record.append(j.text)  #將標籤中的內容加入串列record
    #將一筆資料加入串列lst（不要record的第0個元素，因為它是空白）
    lst.append(record[1:])

#定義欄位名稱
fields = ['年月', '機關', '0-2', '2-4', '4-6', '6-8', '8-10', '10-12',
          '12-14', '14-16', '16-18', '18-20', '20-22', '22-24']

#將資料轉換成DataFrame
df = pd.DataFrame(lst, columns=fields)
df.index += 1   #資料的順序從1開始

result = []   #用以存取每一個時間別所發生交通意外次數的串列
for i in range(2, 14):
    #將每一個時間別欄位的數據加總並加入串列result
    result.append(df[fields[i]].astype('int').sum())
    print(fields[i]+':', result[i-2])   #顯示加總的結果

#顯示最常發生交通事故的時間別
print('每月新北市A1類道路最常發生交通事故的時間別是：%s(%d)' % (fields[result.
index(max(result))+2], max(result)))