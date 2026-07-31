import sqlite3

conn = sqlite3.connect('mydatabase.db')

conn.execute("""
INSERT INTO clientes (nome, email, telefone)
VALUES('João Silva',
        'joao@email.com',
          '(81) 99999-9999')
 """)

conn.execute("""
INSERT INTO clientes (nome, email, telefone)
VALUES('Marcelo Augusto',
        'marcelo@email.com',
          '(81) 99999-8888')
 """)

conn.execute("""
INSERT INTO clientes (nome, email, telefone)
VALUES('Gabriela Barbosa',
        'gabriela@email.com',
          '(81) 99999-7777')
 """)

conn.commit()

conn.close()
