import os

from flask import Flask, redirect, url_for
from flask import Flask
from flask import render_template
from flask import request

import sqlite3


con = sqlite3.connect('entregas.db')
con = con.cursor()

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'lucas'

@app.route('/criar')
def fazer():
	criar()

def criar():
	con = sqlite3.connect('entregas.db')
	con.execute("""
		CREATE TABLE cliente(
		cpf VARCHAR(12) NOT NULL,
		nome_cliente VARCHAR(150) NOT NULL,
		nome_carro VARCHAR(100) NOT NULL,
		final_chassi INTEGER NOT NULL,
		nome_vendedor VARCHAR(150) NOT NULL,
		data_entrega VARCHAR(10) NOT NULL,
		acessorios VARCHAR(200) NOT NULL,
		emplacamento VARCHAR(20) NOT NULL);
		 """)
	con.close()	
@app.route('/')
def index():
	return render_template('form_cadastro_de_carros.html')

@app.route('/listar', methods=["GET", "POST"])
def lista():
	con = sqlite3.connect('entregas.db')
	con = con.cursor()
	con.execute("""SELECT * from cliente """)
	data = con.fetchall()

	return render_template('listar_carros_entrega.html', data = data)


@app.route('/home', methods=["GET", "POST"])
def home():
	
	if request.method == 'POST':
		cpf = request.form['cpf']
		nome_cliente = request.form['nome_cliente']
		nome_carro = request.form['nome_carro']
		final_chassi = request.form['final_chassi']
		nome_vendedor = request.form['nome_vendedor']
		data_entrega = request.form['data_entrega']
		acessorios = request.form['acessorios']
		emplacamento = request.form['emplacamento']
		
		con = sqlite3.connect('entregas.db')

		#teste = (cpf, nome_cliente, nome_carro, final_chassi, nome_vendedor, data_entrega, acessorios, emplacamento)
		con.execute('INSERT INTO cliente(cpf,nome_cliente,nome_carro,final_chassi,nome_vendedor,data_entrega,acessorios,emplacamento) values (?, ?, ?, ?, ?, ?, ?,?)', (cpf,nome_cliente,nome_carro,final_chassi,nome_vendedor,data_entrega,acessorios,emplacamento))
		#db.session.add(teste)
		con.commit()
		con.close()
	#db.query.all()
	return redirect(url_for('lista'))

if __name__ == "__main__":
	app.run(debug=True)