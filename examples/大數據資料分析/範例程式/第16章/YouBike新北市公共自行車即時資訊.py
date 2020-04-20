import requests as rq   #載入requests套件，縮寫rq

#開放資料：'YouBike臺北市公共自行車即時資訊'
url = 'http://data.ntpc.gov.tw/od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=json'

html_content = rq.get(url)   #向html提出get請求

json_data = html_content.json()   #將回傳內容轉換成json格式

'''
#資料欄位說明
sno：站點代號
sna：場站名稱(中文)
tot：場站總停車格
sbi：場站目前車輛數量
sarea：場站區域(中文)
mday：資料更新時間
lat：緯度
lng：經度
ar：地(中文)
sareaen：場站區域(英文)
snaen：場站名稱(英文)
aren：地址(英文)
bemp：空位數量
act：全站禁用狀態 
'''

#item_detail是tuple的第二個元素，形態為字典
for item_detail in json_data:
    print_info = '站點：' + item_detail['sna'] + '，' + \
                 '地址：' + item_detail['ar'] + '，' + \
                 '總停車格：' + item_detail['tot'] + '，' + \
                 '場站目前車輛數量：' + item_detail['sbi'] + '，' + \
                 '空位數量：' + item_detail['bemp'] + '，' + \
                 '資料更新時間：' + item_detail['mday']
    print(print_info)   #顯示結果