import os
import comtypes.client

#PDF檔案格式
wdFormatPDF = 17
#取得目標檔案絕對路徑
in_file = os.path.abspath('wordfile1.docx')
#取得輸出檔案絕對路徑
out_file = os.path.abspath('wordfile1.pdf')
#建立Word物件
word = comtypes.client.CreateObject('Word.Application')
#以Word開啟目標檔案
doc = word.Documents.Open(in_file)
#以Word中另存新檔的功能將檔案另存為PDF檔
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
#關閉檔案
doc.Close()
#關閉Word
word.Quit()