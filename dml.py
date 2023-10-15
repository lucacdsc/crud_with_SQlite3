import sqlite3


connection = sqlite3.connect('base.db')

cur = connection.cursor()

def db_insert(name,contact,color):
    return """
INSERT INTO users (name, contact, color) VALUES ('{}', '{}', '{}')
""".format(name,contact,color)

def db_update(novo_valor,identifier):
    return """
UPDATE users SET name = '{}' WHERE ID = {}
""".format(novo_valor,identifier)

def db_delete(identifier):
    return """
    DELETE FROM users WHERE ID = {}
""".format(identifier)

def db_select(identifier):
    return """
SELECT * FROM users WHERE ID = {}
""".format(identifier)

#cur.execute(db_insert('Mingau','974164619','blue'))
#cur.execute(db_update('lcdsc',1))
#cur.execute(db_delete(2))
cur.execute(db_select(1))
#connection.commit()
data = cur.fetchone()
connection.close()
print(data)