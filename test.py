import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
print ("数据库打开成功")

cursor = c.execute("SELECT message from Messages WHERE sender='James' AND receiver='WentaoGao'")
for row in cursor:
     print(row[0])
