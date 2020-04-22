import xml.etree.cElementTree as ET

#建立class3A標籤
class3A = ET.Element("class3A")

#建立第一位學生的資料
student = ET.SubElement(class3A, "student")
ET.SubElement(student, "name").text = "David"
ET.SubElement(student, "address").text = "New Taipei City"

#建立第一位學生的資料
student = ET.SubElement(class3A, "student")
ET.SubElement(student, "name").text = "Kenny"
ET.SubElement(student, "address").text = "Taichung City"

#建立第一位學生的資料
student = ET.SubElement(class3A, "student")
ET.SubElement(student, "name").text = "Bob"
ET.SubElement(student, "address").text = "Taoyuan City"

#將所有元素建立成元素樹
tree = ET.ElementTree(class3A)
#將資料寫進檔案
tree.write("class3A.xml")