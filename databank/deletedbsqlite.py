import sqlite3

conn = sqlite3.connect("mydatabase.db")

conn.execute(""" 
DELETE FROM clientes
WHERE id = 3
""")

conn.commit()

conn.close()
