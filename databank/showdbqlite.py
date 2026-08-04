import sqlite3

conn =  sqlite3.connect("mydatabase.db")

cursor = conn.execute("SELECT * FROM clientes")

for cliente in cursor:
    print(cliente)


conn.close()
