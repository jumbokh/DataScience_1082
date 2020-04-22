import json

#打開eduagency.json檔
with open('eduagency.json', encoding='utf8') as file:
    data = json.load(file) #將檔案內容轉換成Dictionary
    #印出每一筆資料的運動中心名稱、地址和營運時間
    for record in data:
        print('運動中心：%s' % record['o_tlc_agency_name'])
        print('地址：%s' % record['o_tlc_agency_address'])
        print('營運時間：%s' % record['o_tlc_agency_opentime'])
        print()