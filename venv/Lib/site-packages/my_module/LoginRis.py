import sqlite3

def create_database():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        phone_number TEXT PRIMARY KEY,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL)''')
    
    conn.commit()
    print("connect successfully")
    return conn

def connect_db():
    conn = sqlite3.connect("appOanTuTi_data.db")
    return conn