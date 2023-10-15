import sqlite3

connection = sqlite3.connect('base.db') 

cur = connection.cursor()

sql = """
CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL ,
contact TEXT NOT NULL,
color TEXT UNIQUE NOT NULL)"""

cur.execute(sql)
connection.commit()
connection.close()