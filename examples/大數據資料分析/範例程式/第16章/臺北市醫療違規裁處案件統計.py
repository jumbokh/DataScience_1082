import requests as rq   #載入requests套件

#臺北市醫療違規裁處案件統計
url = 'http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=3761afee-9059-4630-bb41-1c57682cff10'
r = rq.request('GET', url)   #對url發出GET請求

j = r.json()   #將資料轉換成json格式

#取出原始資料中的主要資料，得到的結果是一個串列
j = j['result']['results']

for record in j:
    #抓取罰鍰金額大於六萬元的案子
    if eval(record['罰鍰金額'].replace(',', '')) >= 60000:
        print('區域：', record['區域'])
        print('違規情節：', record['違規情節'])
        print('--------------------------------------------------------------')