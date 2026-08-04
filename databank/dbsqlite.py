import sqlite3

conn = sqlite3.connect('mydatabase.db')

conn.execute("""
CREATE TABLE clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    telefone TEXT
    )
     """)

conn.commit()

conn.close()
