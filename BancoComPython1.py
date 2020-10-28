import sqlite3, os, random, time

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
def data_insert_var():
    new_date = datetime.datetime.now()
    new_prod_name = "Monitor"
    new_valor = random.randrange(50,100)
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?,?,?)",(new_date, new_prod_name, new_valor))
    con.commit()
for i in range (10):
    data_insert_var()
    time.sleep(1)