import requests
import csv
# 網站每3小時更新一次資訊
# 因此以將本程序掛載於排程中
# 即可長期收集氣溫資料 (以下僅保留松山區為例)

url=\
"http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=1f1aaba5-616a-4a33-867d-878142cac5c4"

jsondata = requests.get(url).json()

# 資料輸出檔案儲存位置
csv_output = 'C:\\Users\\Bright\\Desktop\\output.csv'

# 以附加模式(append)輸出至檔案
with open(csv_output, 'a', newline='') as out:
    writer = csv.writer(out, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONE)
    # write header
    writer.writerow(['dataTime', 'locationName', 'geocode', 
                    'value'])

    for row in jsondata["result"]["results"]:
        locationName = row["locationName"]        
        geocode = row["geocode"]
        value = row["value"]
        dataTime = row["dataTime"]
        
        # 螢幕顯示
        print("loc:", dataTime, " " , locationName, " ", 
                                     geocode, " ", value)
        if(locationName=='松山區'):
            # 寫入至檔案
            writer.writerow([dataTime, locationName, geocode, 
                              value])