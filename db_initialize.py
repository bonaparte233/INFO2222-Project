import sqlite3
con = sqlite3.connect('database.db')
con.execute("DROP TABLE IF EXISTS Users;")
con.execute("CREATE TABLE Users (username VARCHAR(200) PRIMARY KEY, password VARCHAR(200), admin CHAR(1))")
con.execute("INSERT INTO Users (username, password, admin) VALUES ('WentaoGao', '123456', '1')")
con.commit()

con.execute("DROP TABLE IF EXISTS Mailbox;")
con.execute("CREATE TABLE Mailbox (sender VARCHAR(200) REFERENCES Users(username), receiver VARCHAR(200) REFERENCES Users(username), content VARCHAR(400))")
