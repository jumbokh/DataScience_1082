import csv

#讀取檔案
with open('20180511臺北市肇事路口.csv') as file:
    #以csv解讀器解讀檔案
    data = csv.reader(file)
    #加總包含"民權西路"的事故件數
    result = sum([eval(record[2]) \
                  for record in data \
                  if '民權西路' in record[1]])
    print('民權西路的事故總件數：%d' % result)