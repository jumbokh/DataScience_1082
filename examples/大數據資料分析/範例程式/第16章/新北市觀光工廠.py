import requests as rq   #載入requests套件，縮寫為rq
from xml.etree import ElementTree   #載入ElementTree套件
import pandas as pd   #載入pandas套件，縮寫為pd

#新北市觀光工廠
url = 'http://data.ntpc.gov.tw/od/data/api/57EB9B00-979C-44BB-A4EE-CC55BDF1488A?$format=xml'
r = rq.request('GET', url)   #對url發出get請求

#將資料的內容轉換成一棵元素樹（ElementTree）
tree = ElementTree.fromstring(r.content)
list_data = []   #用以存放轉換成串列的資料
for i in tree.iter('row'):   #針對ElementTree的每一個row標籤
    single_record = []   #儲存一筆轉換成串列的資料
    for j in i.iter():   #再針對裡面包含的每一個標籤
        #只需要'名稱'、'特色'、'電話'、'地址'
        if j.tag == 'title' or j.tag =='features' or j.tag =='tel' or j.tag == 'address':
            #將符合條件的資料加入串列中
            single_record.append(j.text)
        #將每一筆已轉換成串列的資料加入整個資料集的串列
list_data.append(single_record)

#將資料轉換成Data Frame
df = pd.DataFrame(list_data, columns=['名稱','特色','電話','地址'])
df.index += 1   #資料順序從1開始
print(df)   #顯示結果