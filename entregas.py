import sqlite3

conn = sqlite3.connect('entregas.db')
entregas = conn.cursor()
entregas.execute("""CREATE TABLE entrega(cpf INTEGER(12) NOT NULL PRIMARY KEY , 
	nome_cliente VARCHAR(20) NOT NULL, nome_carro VARCHAR(20) NOT NULL , final_chassi INTEGER(4) NOT NULL, nome_vendedor VARCHAR(10) NOT NULL, 
	data_entrega DATE NOT NULL, emplacamento VARCHAR(20) NOT NULL);""")

conn.commit()

print("Banco criado!!!!")
conn.close()
