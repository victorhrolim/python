import sqlite3

conn = sqlite3.connect('mydatabase.db')

conn.execute("""
INSERT INTO clientes (nome, email, telefone)
VALUES('Gabriela Barbosa',
        'gabriela@email.com',
          '(81) 99999-7777')
""")

conn.execute("""
INSERT INTO clientes (nome, email, telefone)
VALUES('Marcos Augusto',
        'marcos@gmail.com',
          '(81) 99999-6666')
""")

conn.execute("""
INSERT INTO clientes (nome, email, telefone)
VALUES('Rodrigo Garoto',
        'rodrigogaroto@yahoo.com',
          '(81) 99999-5555')
""")

conn.commit()

conn.close()
