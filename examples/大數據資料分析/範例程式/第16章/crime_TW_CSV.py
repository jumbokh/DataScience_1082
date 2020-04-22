import requests
import pandas as pd
# http://data.gov.tw/node/14200
# 每季初步統計提供
# 資料集提供機關名稱: 警政署

#10501-10503
#url = 
"https://quality.data.gov.tw/dq_download_csv.php?nid=14200&md5_url= a40828c836192571d12f4faea9d96790"
url = r"C:\\Users\\Apple\\Desktop\\10501-10503.csv"
crime1 = pd.read_csv(url, encoding="utf-8")

#10504-10506
#url = "https://quality.data.gov.tw/dq_download_csv.php?nid=14200&md5_url=c31da28b393c9c1d58f947dff34491ca"
url = r"C:\\Users\\Apple\\Desktop\\10504-10506.csv"
crime2 = pd.read_csv(url, encoding="utf-8")

#10507-10509
#url = "https://quality.data.gov.tw/dq_download_csv.php?nid=14200&md5_url=d54e0d59b43e817446899074e76c53af"
url = r"C:\\Users\\Apple\\Desktop\\10507-10509.csv"
crime3 = pd.read_csv(url, encoding="utf-8")
print('3')
#10510-10512
#url = "https://quality.data.gov.tw/dq_download_csv.php?nid=14200&md5_url=7ad200450e9b62085f770d2350378c08"
url = "C:\\Users\\Apple\\Desktop\\10510-10512犯罪資料.csv"
crime4 = pd.read_csv(url, encoding="utf-8")

# 各季資料合併
frames = [pd.DataFrame(crime1), pd.DataFrame(crime2), pd.DataFrame(crime3),
pd.DataFrame(crime4)]
df = pd.concat(frames)

# 設定顯示前n名
nShowTop = 5

# Sort by Location
df['發生地點'] = df['發生地點'].str[0:3]
counts_df = pd.DataFrame(df.groupby('發生地點').size().rename('counts'))
sorted = counts_df.sort_values(by='counts', ascending=0)
 
print('<<<<< 犯罪統計前', nShowTop, '名地區 >>>>>')
nLoop = 1
for name, counts in sorted.iterrows():
    print('第', nLoop, '名 - ', name, ' ', counts[0], '次')
    nLoop = nLoop + 1
    if nLoop > nShowTop:
        break
print()
        
# Sort by Month
df['發生月份'] = df['發生日期'].astype(str).str[3:5]
counts_df = pd.DataFrame(df.groupby('發生月份').size().rename('counts'))
sorted = counts_df.sort_values(by='counts', ascending=0)
 
print('<<<<< 犯罪統計前', nShowTop, '名月份 >>>>>')
nLoop = 1;
for name, counts in sorted.iterrows():
    print('第', nLoop, '名 - ', name, ' ', counts[0], '次')
    nLoop = nLoop + 1
    if nLoop > nShowTop:
        break
print()