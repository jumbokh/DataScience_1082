import sqlite3
import csv

#連結資料庫檔案
con = sqlite3.connect('myDB2.db')

#建立cursor物件
c = con.cursor()

#建立groups資料表的查詢指令
create_groups = 'CREATE TABLE groups ( \
 group_id int primary key not null, \
 group_name char(50) not null \
);'
c.execute(create_groups)

#建立students資料表的查詢指令
create_students = 'CREATE TABLE students ( \
 student_id int primary key not null, \
 student_name char(50) not null, \
 group_id int not null, \
 FOREIGN KEY (group_id) REFERENCES groups (group_id) \
 ON DELETE NO ACTION ON UPDATE NO ACTION \
);'
c.execute(create_students)

#為groups資料表新增資料
c.execute("INSERT INTO groups (group_id, group_name) VALUES (1, '青色之馬');")
c.execute("INSERT INTO groups (group_id, group_name) VALUES (2, '夢幻之都');")
c.execute("INSERT INTO groups (group_id, group_name) VALUES (3, '新不了城');")

students = []
#讀取students.csv中的資料並將其將入students資料表中
with open('students.csv', encoding='utf8') as file:
    students = list(csv.reader(file, delimiter=','))
    for student in students[1:]:
        c.execute("INSERT INTO students (student_id, student_name, group_id) \
          VALUES (%d, '%s', %d);" % (eval(student[0]), student[1], eval(student[2])))

#確認新增
con.commit()

#執行查詢students資料表中屬於第3組的同學的學號、名字、組號和組名
cursor = c.execute("SELECT S.*, G.group_name \
                   FROM students S, groups G \
                   WHERE S.group_id = G.group_id \
                   AND S.group_id = 3")

#檢視查詢結果
for record in cursor:
    print(record)

#關閉與資料庫的連結
con.close()