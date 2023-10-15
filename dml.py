import sqlite3

def commit_close(func):
    def decorator(*args):
        connection = sqlite3.connect('base.db')
        cur = connection.cursor()
        sql = func(*args)
        cur.execute(sql)
        connection.commit()
        connection.close()
    return decorator

@commit_close
def db_insert(name,contact,color):
    return """
INSERT INTO users (name, contact, color) VALUES ('{}', '{}', '{}')
""".format(name,contact,color)

@commit_close
def db_update(novo_valor,identifier):
    return """
UPDATE users SET name = '{}' WHERE ID = {}
""".format(novo_valor,identifier)


@commit_close
def db_delete(identifier):
    return """
    DELETE FROM users WHERE ID = {}
""".format(identifier)

def db_select(identifier):
    connection = sqlite3.connec('base.db')
    cur = connection.cursor()
    sql = """
SELECT * FROM users WHERE ID = {}
""".format(identifier)
    cur.execute(sql)
    data = cur.fetchall()
    connection.close()
    return data

