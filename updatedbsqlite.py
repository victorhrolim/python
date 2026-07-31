import sqlite3

conn = sqlite3.connect("mydatabase.db")

conn.execute(""" 
UPDATE clientes
SET telefone = '(81) 9999-9998'
WHERE id = 1
""")

conn.commit()

conn.close()
