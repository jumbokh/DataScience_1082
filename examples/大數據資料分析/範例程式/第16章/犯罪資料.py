import requests as rq   #載入requests套件，縮寫為rq
import pandas as pd   #載入pandas套件，縮寫為pd

#載入ElementTree套件，縮寫為ET
from xml.etree import ElementTree as ET

#犯罪資料
url = 'http://data.ntpc.gov.tw/od/data/api/314C5A69-7ED3-469E-AB05-08ABE613BFC9?$format=xml'
r = rq.request('GET', url)   #對url發出get請求

#將得到的資料轉換成一棵元素樹（ElementTree）
xml_data = ET.fromstring(r.content)

list_data = []   #用以存放全部資料的資料集串列
for record in xml_data.iter('row'):   #針對每一筆資料
    lst = []   #存放每一筆資料的內容
    #將單一個'row'標籤中的每一個標籤的內容加到串列中
    for col in record.iter():
        lst.append(col.text)
    #將已經轉換成串列的每一筆資料加入到資料集串列，去掉第0筆（內容空白）
    list_data.append(lst[1:4])

#將資料集串列轉換成Data Frame
df = pd.DataFrame(list_data, columns=['案類','發生日期','發生地區'])
df.index += 1   #資料順序從1開始
print(df)