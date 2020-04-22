import xml.etree.ElementTree as ET
tree = ET.parse('company.xml') #將檔案內容轉換成元素樹
root = tree.getroot() #取得樹根

#輸出每個部門的相關資訊
for dept in root.findall('department'):
    print('Department name: %s' % dept.find('name').text)
    print('Members: %s' % dept.find('members').text)
    print('Manger: %s' % dept.find('manager').text)
    print()