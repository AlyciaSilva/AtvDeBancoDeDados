import os
import sqlite3

os.remove("alycia.db") if os.path.exists ("alycia.db") else None
con = sqlite3.connect('alycia.db')
print(type(con))
cur = con.cursor()
print(type(cur))
slq_create = ' create table informacoes '\
             '(email varchar primary key, '\
             'nome  char(50), ' \
             'telefone integer(9))'

cur.execute(slq_create)
sql_insert = 'insert into informacoes values (?, ?, ?)'
recset = [
    ('Simonelima@gmail.com','Simone', 987852209),
    ('Alycialima@gmail.com','Alycia', 985623547),
    ('Samarasantos@gmail.com','Samara', 936547852),
    ('Santos@gmail.com','Santos', 936533852)
]
for rec in recset:
    cur.execute(sql_insert, rec)
def create_table():
    cur.execute('CREATE TABLE IF NOT EXITIS produtos(id INTERGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
        'prod_name TEXT, valor REAL)')
def data_insert():
    cur.execute("INSERT INTO produtos VALUES(10, '2020-05-02 14:32:11', 'teclado', 90)")
con.commit()
cur.close()
con.close()