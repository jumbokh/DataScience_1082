import sqlite3

#連結資料庫檔案
con = sqlite3.connect('myDB.db')

#建立cursor物件
c = con.cursor()

#建立資料表的查詢指令
createStr = 'CREATE TABLE Employee\
       (ID INT PRIMARY KEY     NOT NULL,\
       NAME           TEXT    NOT NULL,\
       BIRTHYEAR      INT     NOT NULL,\
       ADDRESS        CHAR(50),\
       SALARY         INT);'
#執行建立資料表的指令
c.execute(createStr)

#新增資料至資料表
c.execute("INSERT INTO Employee (ID, NAME, BIRTHYEAR, ADDRESS, SALARY) \
      VALUES (1, '小陳', 1997, '新北市', 58000 )")
c.execute("INSERT INTO Employee (ID, NAME, BIRTHYEAR, ADDRESS, SALARY) \
      VALUES (2, '小范', 2000, '臺北市', 50000 )")
c.execute("INSERT INTO Employee (ID, NAME, BIRTHYEAR, ADDRESS, SALARY) \
      VALUES (3, '小施', 1999, '高雄市', 47000 )")
c.execute("INSERT INTO Employee (ID, NAME, BIRTHYEAR, ADDRESS, SALARY) \
      VALUES (4, '小吳', 1998, '台中市', 52000 )")

#確認新增
con.commit()

#執行查詢Employee資料表的所有內容
cursor = c.execute("SELECT * from Employee")

#檢視查詢結果
for record in cursor:
    print(record)

#關閉與資料庫的連結
con.close()