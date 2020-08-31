import sqlite3

conn = sqlite3.connect('entregas.db')
entregas = conn.cursor()
v=input("O que você deseja fazer? INSERIR(i), DELETAR(d), ATUALIZAR/EDITAR(at), LISTAR TODOS(v): ").lower()
'''#ALTERAR COLUNA
if v=="a":
	def alterar_add():
		entregas.execute("""ALTER TABLE aluno ADD COLUMN endereco VARCHAR(255) """)
		conn.commit()
	print("Alteração concluida com sucesso!")
	alterar_add()'''

#INSERIR DADOS
if v=="i":
	
	def inserir(cpf,nome_cliente,nome_carro,final_chassi,nome_vendedor,data_entrega,emplacamento):
		entregas.execute("""INSERT INTO entrega values(?,?,?,?,?,?,?)""",(cpf,nome_cliente,nome_carro,final_chassi,nome_vendedor,data_entrega,emplacamento))

		conn.commit()

	cpf=input("Insira o cpf do cliente: ")
	nome_cliente=input("Insira o nome do cliente: ")
	nome_carro=input("Insira o nome do carro: ")
	final_chassi=input("Insira os quatro ultimos digitos do chassi: ")
	nome_vendedor=input("Insira o nome do vendedo: ")
	data_entrega=input("Insira a data da entrega Ex:(2020-09-10): ")
	emplacamento=input("Insira o emplacamento (Interno ou externo): ")

	inserir(cpf,nome_cliente,nome_carro,final_chassi,nome_vendedor,data_entrega,emplacamento)

#DELETAR DADOS
if v=="d":
	def deletar(cpf):
		entregas.execute("""DELETE from entrega where cpf=?""",(cpf,))
		conn.commit()
	l=int(input("Digite o cpf do cliente para deletar a entrega: "))
	deletar(l)

#ATUALIZAR DADOS
if v=="at":
	funcoes=input("QUAL DOS PARAMETROS DESEJA EDITAR? NOME DO CARRO(nc), FINAL DO CHASSI(fc), NOME DO VENDEDOR(nv), DATA DE ENTREGA(de): ").lower()
	if funcoes=="nc":
		def atualizar_nome_carro (nome_carro,cpf):
			entregas.execute("""UPDATE entrega set nome_carro= ? where cpf=?""",(nome_carro,cpf))
			conn.commit()
		f=input("Insira o nome do carro: ")
		cp=input("Digite o cpf do cliente da sua edição: ")
		atualizar_nome_carro(f,cp)

	if funcoes=="fc":
		def atualizar_final_chassi (final_chassi,cpf):
			entregas.execute("""UPDATE entrega set final_chassi= ? where cpf=?""",(final_chassi,cpf))
			conn.commit()
		f=input("Insira O final do chassi: ")
		cp=input("Digite o cpf do cliente da sua edição: ")
		atualizar_final_chassi(f,cp)

	if funcoes=="nv":
		def atualizar_nome_vendedor (nome_vendedor,cpf):
			entregas.execute("""UPDATE entrega set nome_vendedor= ? where cpf=?""",(nome_vendedor,cpf))
			conn.commit()
		f=input("Insira o nome do vendedo: ")
		cp=input("Digite o cpf do cliente da sua edição: ")
		atualizar_nome_vendedor(f,cp)

	if funcoes=="de":
		def atualizar_data (data_entrega,cpf):
			entregas.execute("""UPDATE entrega set data_entrega= ? where cpf=?""",(data_entrega,cpf))
			conn.commit()
		f=input("Insira a data da entrega Ex:(2020-09-10): ")
		cp=input("Digite o cpf do cliente da sua edição: ")
		atualizar_data(f,cp)

	

#VER DADOS
if v=="v":
	def ver_dados():
		entregas.execute("""SELECT * from entrega """)
		for linha in entregas.fetchall():
			print("|CPF | NOME CLIENTE | NOME CARRO | FINAL CHASSI | NOME DO VENDEDOR | DATA DA ENTREGA | EMPLACAMENTO| ")
			print("")
			print(linha)
			print("")
	ver_dados()
		

print("DADOS ATUALZADOS NO BANCO DE DADOS")
conn.close()
