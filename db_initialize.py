import sqlite3
con = sqlite3.connect('database.db')
con.execute("DROP TABLE IF EXISTS Users;")
con.execute("CREATE TABLE Users (username VARCHAR(200) PRIMARY KEY, password VARCHAR(200), admin CHAR(1))")
con.execute("INSERT INTO Users (username, password, admin) VALUES ('WentaoGao', '123456', '1')")
con.execute("INSERT INTO Users (username, password, admin) VALUES ('James', '123456', '1')")
con.commit()

con.execute("DROP TABLE IF EXISTS Friends;")
con.execute("CREATE TABLE Friends (friend_r VARCHAR(200), friend_a VARCHAR(200))")
con.execute("INSERT INTO Friends (friend_r, friend_a) VALUES ('WentaoGao', 'James')")
con.execute("INSERT INTO Friends (friend_r, friend_a) VALUES ('James', 'WentaoGao')")
con.commit()

con.execute("DROP TABLE IF EXISTS Messages;")
con.execute("CREATE TABLE Messages (sender VARCHAR(200), receiver VARCHAR(200), message VARCHAR(1000))")
con.execute("INSERT INTO Messages (sender, receiver, message) VALUES ('WentaoGao', 'James', 'Hi')")
con.execute("INSERT INTO Messages (sender, receiver, message) VALUES ('James', 'WentaoGao', 'Hello')")
con.commit()
