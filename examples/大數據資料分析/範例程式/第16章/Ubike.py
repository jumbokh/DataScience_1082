import sys
import json
import requests

url = 'http://data.taipei/youbike'
data = requests.get(url).content.decode("utf-8")

jsondata = json.loads(data)
#sno：站點代號
#sna：場站名稱(中文)
#tot：場站總停車格
#sbi：場站目前車輛數量
#sarea：場站區域(中文)
#mday：資料更新時間
#lat：緯度
#lng：經度
#ar：地(中文)
#sareaen：場站區域(英文)
#snaen：場站名稱(英文)
#aren：地址(英文)
#bemp：空位數量
#act：全站禁用狀態
for key, value in jsondata["retVal"].items():
    detail = value
    sna = value["sna"]
    sbi = value["sbi"]
    bemp = value["bemp"]
    act = value["act"]
    mday = value["mday"]
    row = "站名:"+ key+" " + sna+ " 可借:" + sbi+ " 可停:"+ \
          bemp+ " 場站運作中:"+ act
    print(row)
print(row.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))