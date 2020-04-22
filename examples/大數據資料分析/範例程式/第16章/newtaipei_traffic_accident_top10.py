import json
import requests
import pandas as pd

# 資料來源: http://data.ntpc.gov.tw (新北市政府資料開放平台)
# A1類：造成人員當場或二十四小時內死亡之交通事故。

# 設定顯示前n名
nShowTop = 5

def DisplayTopN(Title, Captions, Data):
    print('<<<<< ', Title, '前', nShowTop, '名 >>>>>')
    __nLoop = 1
    for __i, __row in sorted.iterrows():
        print('第', __nLoop, '名 -', Captions[__row.name], 
                 __row[0], '次')
        __nLoop = __nLoop + 1
        if __nLoop > nShowTop:
            break
    print()

def BuildColumnList(Captions):
    __cols = []
    for __i in range(1, len(Captions) - 1):
        __cols.append("field{0}".format(__i))
#    __cols.append("other")
    return(__cols)

def LoadJsonAndSort(url, cols):
    __data = requests.get(url).content.decode("utf-8")
    __jsondata = json.loads(__data)
    
    __df = pd.DataFrame(__jsondata, columns = cols)
    __df = __df.replace([''],[0]).astype(int).sum()
    __sorted = __df.sort_values(ascending=False).to_frame()
    return(__sorted)
    
# 每月新北市A1交通事故車輛種類
# http://data.ntpc.gov.tw/od/detail?oid=03A46914-B774-4C1C-BF75-E6EECE1E311C
# yearmonth：年月、organ：機關、field1：營業大客車、field2：自用大客車、field3：營業小客車、field3：自用小客車、field5：營業大貨車、field6：自用大貨車、field7：營業小貨車、field8：自用小貨車、field9：重型機車、field10：輕型機車、field11：軍用小客車、field12：軍用吉普車、field13：軍用大貨車、other：其他
url = "http://data.ntpc.gov.tw/od/data/api/95752309-8CE8-4C95-AB44-E478920B6696?$format=json"
captions = {'field1':'營業大客車','field2':'自用大客車','field3':'營業小客車','field4':'自用小客車','field5':'營業大貨車','field6':'自用大貨車','field7':'營業小貨車','field8':'自用小貨車','field9':'重型機車','field10':'輕型機車','field11':'軍用小客車','field12':'軍用吉普車','field13':'軍用大貨車','other':'其他'}
sorted = LoadJsonAndSort(url, BuildColumnList(captions))
DisplayTopN('每月新北市A1交通事故車輛種類', captions, sorted)

# 每月新北市A1類道路交通事故－肇事者
# http://data.ntpc.gov.tw/od/detail?oid=0D1DF0FD-D3C6-4438-8C4C-C2AFDB98B31A
# yearmonth:年月organ:機關field1:肇事者(第一當事人)-男field2:肇事者(第一當事人)-女field3:肇事者(第一當事人)-不詳field4:死亡-男field5:死亡-女field6:受傷-男field7受傷－女
# http://data.ntpc.gov.tw/od/data/api/F866700B-D580-4FD2-A4C0-583B5833BC66?$format=json
url = "http://data.ntpc.gov.tw/od/data/api/F866700B-D580-4FD2-A4C0-583B5833BC66?$format=json"
captions = {'field1':'肇事者(第一當事人)-男','field2':'肇事者(第一當事人)-女','field3':'肇事者(第一當事人)-不詳','field4':'死亡-男','field5':'死亡-女','field6':'受傷-男','field7':'受傷－女'}
sorted = LoadJsonAndSort(url, BuildColumnList(captions))
DisplayTopN('每月新北市A1類道路交通事故－肇事者', captions, sorted)

# 每月新北市A1類道路交通事故－肇事時間別
# http://data.ntpc.gov.tw/od/detail?oid=5992155D-41DD-4466-98F3-CA2463835999
# yearmonth:年月、organ:機關、field1:0-2、field2:2-4、field3:4-6、field4:6-8、field5:8-10、field6:10-12、field7:12-14、field8:14-16、field9:16-18、field10:18-20、field11:20-22、field12:22-24
# http://data.ntpc.gov.tw/od/data/api/7D58F2F5-E8E1-4D15-959F-26A16C8384AF?$format=json
url = "http://data.ntpc.gov.tw/od/data/api/7D58F2F5-E8E1-4D15-959F-26A16C8384AF?$format=json"
captions = {'field1':'0-2','field2':'2-4','field3':'4-6','field4':'6-8','field5':'8-10','field6':'10-12','field7':'12-14','field8':'14-16','field9':'16-18','field10':'18-20','field11':'20-22','field12':'22-24'}
sorted = LoadJsonAndSort(url, BuildColumnList(captions))
DisplayTopN('每月新北市A1類道路交通事故－肇事時間別', captions, sorted)

# 每月新北市A1類道路交通事故－原因及傷亡
# http://data.ntpc.gov.tw/od/detail?oid=FFA7DDCD-6B99-4268-A4B0-E35D8542FF45
# yearmonth:年月、organ:機關、field1:駕駛人過失-超速失控(含未減速)、field2:駕駛人過失-酒後駕車、field3:駕駛人過失-未注意車前狀況、field4:駕駛人過失-肇事逃逸、field5:駕駛人過失-未保持行車安全間距、field6:駕駛人過失-未依規定讓車field7駕駛人過失-行駛疏忽、field8:駕駛人過失－違反號誌管制、field9:駕駛人過失-違反標誌標線、field10:駕駛人過失-逆向行駛、field11:駕駛人過失-轉彎不當、field12:駕駛人過失-搶越行人穿越道、field13:駕駛人過失-其他、field14:機件故障、field15:行人過失、field16:交通管制設施缺陷、other:其他
# http://data.ntpc.gov.tw/od/data/api/15A0EB13-E0D7-484E-9997-B747500557D2?$format=json
url = "http://data.ntpc.gov.tw/od/data/api/15A0EB13-E0D7-484E-9997-B747500557D2?$format=json"
captions = {'field1':'駕駛人過失-超速失控(含未減速)','field2':'駕駛人過失-酒後駕車','field3':'駕駛人過失-未注意車前狀況','field4':'駕駛人過失-肇事逃逸','field5':'駕駛人過失-未保持行車安全間距','field6':'駕駛人過失-未依規定讓車','field7':'駕駛人過失-行駛疏忽','field8':'駕駛人過失－違反號誌管制','field9':'駕駛人過失-違反標誌標線','field10':'駕駛人過失-逆向行駛','field11':'駕駛人過失-轉彎不當','field12':'駕駛人過失-搶越行人穿越道','field13':'駕駛人過失-其他','field14':'機件故障','field15':'行人過失','field16':'交通管制設施缺陷','other':'其他'}
sorted = LoadJsonAndSort(url, BuildColumnList(captions))
DisplayTopN('每月新北市A1類道路交通事故－原因及傷亡', captions, sorted)

# 每月新北市A1類道路交通事故-道路類別
# http://data.ntpc.gov.tw/od/detail?oid=3D8BF787-F435-4C26-A50F-762A4FC112A5
# yearmonth:年月、organ:機關、field1:國道(高速公路)、field2:省道、field3:縣道、field4:鄉道、field5:市區道路、field6:村里道路、field7:專用道路、other:其他
# http://data.ntpc.gov.tw/od/data/api/C79E1179-20AF-422B-8827-D71C696F45F4?$format=json
url = "http://data.ntpc.gov.tw/od/data/api/C79E1179-20AF-422B-8827-D71C696F45F4?$format=json"
captions = {'field1':'國道(高速公路)','field2':'省道','field3':'縣道','field4':'鄉道','field5':'市區道路','field6':'村里道路','field7':'專用道路','other':'其他'}
sorted = LoadJsonAndSort(url, BuildColumnList(captions))
DisplayTopN('每月新北市A1類道路交通事故-道路類別', captions, sorted)

# 每年新北市A1交通事故道路類別及道路型態別
# http://data.ntpc.gov.tw/od/detail?oid=041FBDA5-2FA7-4AF8-AB37-3D9A3CFEBCDF
# year:年度、organ:機關別、field1:國道、field2:省道、field3:縣道、field4:鄉道、field5:市區道路、field6:村里道路、field7:專用道路、field8:其他、 field9:平交道、field10:交叉路、field11:隧道、field12:地下道、field13:橋樑、field14:涵洞、field15:高道架路、field16:彎曲路及附近、field17:坡路、 field18:巷弄、field19:直路、field20:其他、field21:圓環、field22:廣場
# http://data.ntpc.gov.tw/od/data/api/31BD85BF-6FFC-48BC-8807-AE5CAEC489EC?$format=json
url = "http://data.ntpc.gov.tw/od/data/api/31BD85BF-6FFC-48BC-8807-AE5CAEC489EC?$format=json"
captions = {'field1':'國道','field2':'省道','field3':'縣道','field4':'鄉道','field5':'市區道路','field6':'村里道路','field7':'專用道路','field8':'其他','field9':'平交道','field10':'交叉路','field11':'隧道','field12':'地下道','field13':'橋樑','field14':'涵洞','field15':'高道架路','field16':'彎曲路及附近','field17':'坡路','field18':'巷弄','field19':'直路','field20':'其他','field21':'圓環','field22':'廣場'}
sorted = LoadJsonAndSort(url, BuildColumnList(captions))
DisplayTopN('每年新北市A1交通事故道路類別及道路型態別', captions, sorted)

# 每月新北市A1類道路交通事故－乘坐車種及死傷人數
# http://data.ntpc.gov.tw/od/detail?oid=96AA9966-73B0-445E-A82D-BEBAADC51973
# yearmonth:年月、district:區、people:人數、field1:大貨車、field2:小貨車、field3:大客車、field4:營業小客車、field5:自用小客車、field6:特種車、field7:機踏車、field8:行人、field9:其他
# http://data.ntpc.gov.tw/od/data/api/C058D858-4F3D-42EA-97DD-274C58A2A9B5?$format=json
url = "http://data.ntpc.gov.tw/od/data/api/C058D858-4F3D-42EA-97DD-274C58A2A9B5?$format=json"
captions = {'field1':'大貨車','field2':'小貨車','field3':'大客車','field4':'營業小客車','field5':'自用小客車','field6':'特種車','field7':'機踏車','field8':'行人','field9':'其他'}
sorted = LoadJsonAndSort(url, BuildColumnList(captions))
DisplayTopN('每月新北市A1類道路交通事故－乘坐車種及死傷人數', captions, sorted)

# 每月新北市A1類道路交通事故-道路型態別
# http://data.ntpc.gov.tw/od/detail?oid=42DBA8D0-1A44-48A3-9382-A864497A64FC
# yearmonth:年月、organ:機關、field1:隧道、field2:橋樑、field3:高架道路、field4:彎曲路及附近、field5:坡路、field6:巷道、field7:直路、field8:其他、field9:圓環、field10:廣場
# http://data.ntpc.gov.tw/od/data/api/835FCA61-BCC9-4DB7-AEC7-63A25004EBBA?$format=json
url = "http://data.ntpc.gov.tw/od/data/api/835FCA61-BCC9-4DB7-AEC7-63A25004EBBA?$format=json"
captions = {'field1':'隧道','field2':'橋樑','field3':'高架道路','field4':'彎曲路及附近','field5':'坡路','field6':'巷道','field7':'直路','field8':'其他','field9':'圓環','field10':'廣場'}
sorted = LoadJsonAndSort(url, BuildColumnList(captions))
DisplayTopN('每月新北市A1類道路交通事故-道路型態別', captions, sorted)

# 酒駕肇事傷亡與肇事因素分析統計表
# http://data.ntpc.gov.tw/od/detail?oid=F4CC0B85-91EA-4CF4-9A97-D1D6194AA32D
# year:年度、Parties:第一當事者、field1:違規超車、field2:爭(搶)道行駛、field3:蛇行、方向不定、field4:逆向行駛、field5:未靠右行駛、field6:未依規定讓車、field7:變換車道或方向不當、field8:左轉彎未依規定、
# field9:右轉彎未依規定、field10:迴轉未依規定、field11:橫越道路不慎、field12:倒車未依規定、field13:超速失控、field14:未依規定減速、field15:搶越行人穿越道、field16:未保持行車安全距離、
# field17:未保持行車安全間隔、field18:停車操作時未注意其他車(人)安全、field19:起步未注意其他車(人)安全、field20:吸食違禁物後駕駛失控、field21:酒醉(後)駕駛失控、
# field22:疲勞(患病)駕駛失控、field23:未注意車前狀態、field24:搶(闖)越平交道、field25:違反號誌管制或指揮、field26:違反特定標誌(線)禁制、field27:未依規定使用燈光、
# field28:暗處停車無燈光、標識、field29:夜間行駛無燈光設備、field30:裝載貨物不穩妥、field31:載貨超重而失控、field32:超載人員而失控、field33:貨物超長、寬、高而肇事、
# field34:裝卸貨不當、field35:裝載未盡安全措施、field36:未待乘客安全上下開車、field37:其他裝載不當肇事、field38:違規停車或暫停不當而肇事、field39:拋錨未採安全措施、
# field40:開啟車門不當而肇事、field41:使用手持行動電話失控、field42:其他引起事故之違規或不當行為、field43:不明原因肇事、field44:尚未發現肇事因素、field45:煞車失靈、
# field46:方向操縱系統故障、field47:燈光系統故障、field48:車輪脫落或輪胎爆裂、field49:車輛零件脫落、field50:其他引起事故之故障、field51:穿越道、地下道、未依規定行走行人天橋而穿越道路、
# field52:未依標誌、標線、號誌或手勢指揮穿越道路、field53:穿越道路未注意左右來車、field54:在道路上嬉戲或奔走不定、field55:未待車輛停妥而上下車、field56:上下車輛未注意安全、
# field57:頭手伸出車外而肇事、field58:乘坐不當而跌落、field59:在路上工作未設適當標識、field60:其他引起事故之疏失、field61:路況危險無安全(警告)設施、field62:交通管制設施失靈或損毀、
# field63:交通指揮不當、field64:平交道看守疏失或未放柵欄、field65:其他交通管制不當、field66:動物竄出、field67:尚未發現肇事因素
# http://data.ntpc.gov.tw/od/data/api/55980512-4E1B-4F16-98B9-52EFD0EE0EF5?$format=json