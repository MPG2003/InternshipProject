import sqlite3
conn = sqlite3.connect("exp.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS expenses
           ( date DATE,
            
            description TEXT,
            category TEXT,
            price REAL)""")
conn.commit()

conn.close()