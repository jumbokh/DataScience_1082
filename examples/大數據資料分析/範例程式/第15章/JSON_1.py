import json

#建立資料
data = {}
#欄位people為1串列
data['people'] = []  
data['people'].append({  
    'id': '1',
    'name': 'Peter',
    'country': 'Taiwan'
})
data['people'].append({  
    'id': '2',
    'name': 'Jack',
    'country': 'USA'
})
data['people'].append({  
    'id': '3',
    'name': 'Cindy',
    'country': 'Japan'
})

#將資料寫入檔案
with open('JSON_data.json', 'w') as outfile:  
    json.dump(data, outfile)