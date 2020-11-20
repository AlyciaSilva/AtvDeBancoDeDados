import sqlite3, os, random, time

os.remove("papelaria.db") if os.path.exists ("papelaria.db") else None
con = sqlite3.connect('papelaria.db')
print(type(con))
cur = con.cursor()
print(type(cur))
slq_create = ' create table produtos '\
             '(cod_id varchar primary key, '\
             'prod_name  varchar(50), ' \
             'data  varchar(50), ' \
             'valor char(9))'

cur.execute(slq_create)
slq_create = ' create table cadastro '\
             '(cpf int primary key, '\
             'nome  varchar(50), ' \
             'idade  int(50)), ' 
cur.execute(slq_create)
sql_insert = 'insert into cadastro values (?, ?, ?)'
recset = [
    (13620444447, 'Simone', 22),
    (13620444445,'Alycia', 17),
    (13620456447,'Samara', 52),
    (13880444447,'Santos', 20),
    (13880444487,'Samuel', 60)
]
for rec in recset:
    cur.execute(sql_insert, rec)
def insert():
    new_cod = random.randint(0,9999)
    new_date = datetime.datetime.now()
    new_prod_name = "Nipin"
    new_valor = random.randrange(50,100)
    cur.execute("INSERT INTO produtos (cod_id, prod_name, data, valor) VALUES (?,?,?,?)",(new_cod, new_date, new_prod_name, new_valor))
    con.commit()
for i in range (10):
    insert()
    time.sleep(1)
def consulta_dos_dados():
    cur.execute("SELECT * FROM produtos")
    for linha in cur.fetchall():
        print(linha)
def consulta_de_pessoas_maioresde22():
    cur.execute("SELECT * FROM cadastro WHERE idade > 22")
    for linha in cur.fetchall():
        print(linha)      
def consulta_da_coluna_cpf():
    cur.execute("SELECT * FROM cadastro")
    for linha in cur.fetchall():
        print(linha[0]) 
def atualizando_dados():
    cur.execute("UPDATE produtos SET idade = 50 WHERE idade = 52")
    con.commit()
def removendo_dados():
    cur.execute("DELETE FROM cadastro WHERE idade = 20")
    con.commit()