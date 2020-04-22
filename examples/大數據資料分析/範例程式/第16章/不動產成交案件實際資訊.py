import requests as rq   #載入requests套件，縮寫為rq
import pandas as pd   #載入pandas套件，縮寫為pd

#“不動產成交案件實際資訊”介接網址
url = 'http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=51839ac9-6454-49f2-aaf2-abd05c5405c8'
r = rq.request("GET", url)   #發出HTML GET請求

json_data = r.json()   #將結果轉換成json格式

data = json_data['result']['results']

columns = data[0].keys()   #獲得欄位名稱

values = [x.values() for x in data]   #獲得全部資料

#將json格式資料轉換成Data Frame
df = pd.DataFrame(values, columns = columns)

#處理字串，獲取中文欄位名稱
s = '成交案件類型(CASE_T)、行政區(DISTRICT)、交易標的/租賃標的(CASE_F)、土地區段' \
'位置或建物區門牌(LOCATION)、土地移轉總面積(坪)/土地租賃總面積(坪)(LANDA)、都市土地' \
'使用分區(LANDA_Z)、交易年月(SDATE)、交易筆棟數/租賃筆棟數(SCNT)、移轉層次(SBUILD)' \
'、總樓層數(TBUILD)、建物型態(BUITYPE)、主要用途(PBUILD)、主要建材(MBUILD)、建築完' \
'成年月(FDATE)、建物移轉總面積(坪)/租賃總面積(坪)(FAREA)、建物現況格局_房(BUILD_R)' \
'、建物現況格局_廳(BUILD_L)、建物現況格局_衛(BUILD_B)、建物現況格局_隔間(BUILD_P)、' \
'有無管理組織(RULE)、有無附傢俱(BUILD_C)、交易總價(萬元)/租賃總價(萬元)(TPRICE)、' \
'交易單價(萬元/坪)/租賃單價(元/坪)(UPRICE)、單價是否含車位(UPNOTE)、車位類別及數量' \
'(PARKTYPE)、車位移轉總面積(坪)/車位租賃總面積(坪)(PAREA)、車位移轉總價(萬元)/車位' \
'租賃總價(元)(PPRICE)、備註(RMNOTE)'
lst = s.split('、')

#去掉每個字串最後面的英文縮寫欄位名稱
lst2 = [x[:x.rindex('(')] for x in lst]
lst2.insert(0, 'ID')

#以最新得到的欄位名稱建立DataFrame
df = pd.DataFrame(values, columns = lst2)

#先將欄位“交易單價(萬元/坪)/租賃單價(元/坪)”的值轉換成浮點數
df['交易單價(萬元/坪)/租賃單價(元/坪)'] = df['交易單價(萬元/坪)/租賃單價(元/坪)'].astype('float32')

#獲得各區域的交易單價(萬元/坪)/租賃單價(元/坪)
result = df.groupby(by=['行政區'])['交易單價(萬元/坪)/租賃單價(元/坪)'].sum()
print(result)