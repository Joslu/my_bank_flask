import sqlite3 as sql

DB_PATH = 'users.db'


def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        userId INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')
    conn.commit()
    conn.close()

def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [(0, "usuario", "usuario.com", "1234"),
            (1, "admin", "admin", "admin"),]
    cursor.executemany("""INSERT INTO users VALUES (?, ?, ?, ?)""", data)
    conn.commit()
    conn.close()

def edit_user(user_id = 5, new_name="name",new_email='admin', new_password='admin'):
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE users
        SET name=?, password=?, email=?
        WHERE userId=?
    ''', (new_name, new_password, new_email,user_id))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    print("Starting wohooo")
    createDB()
    addValues()
    ##edit_user()