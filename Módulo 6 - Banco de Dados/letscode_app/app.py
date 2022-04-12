from crypt import methods
from curses import has_key
import os
import re
import dotenv
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from os.path import join, dirname
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, flash, url_for, session, redirect 

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.secret_key = 'auth@flask'

# Conectar ao Banco de Dados Postgres
DB_HOST = os.environ.get("SECRET_DB_HOST")
DB_NAME = os.environ.get("SECRET_DB_NAME")
DB_USER = os.environ.get("SECRET_DB_USER")
DB_PASS = os.environ.get("SECRET_DB_PASS")
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

# Rota Default
@app.route('/', methods=['GET', 'POST'])
def index():
        if 'loggedin' in session:
                return render_template('home.html', nome=session['nome'])
        return redirect(url_for('login'))

# Rota de Login
@app.route('/login/', methods=['GET', 'POST'])
def login():
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if request.method == 'POST' and 'key' in request.form and 'email' in request.form:
                email = request.form['email']
                key = request.form['key']
                cursor.execute('SELECT * FROM users WHERE email = %s', (email))
                account = cursor.fetchone()
                if account:
                        key_postgres = account['key']
                        if check_password_hash(key_postgres, key):
                                session['loggedin'] = True
                                session['id'] = account['id']
                                session['nome'] = account['nome']
                                return redirect(url_for('index'))
                        else:
                                flash('Senha incoreta!')
                return render_template('login.html')

# Rota de Registro de usuário
@app.route('/register/', methods=['GET', 'POST'])
def register():
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if request.method == 'POST' and 'nome' in request.form and 'key' in request.form and 'email' in request.form:
                nome = request.form['nome']
                key = request.form['key']
                email = request.form['email']
                cursor.execute('SELECT * FROM users WHERE email = %s', (email))
                account = cursor.fetchone()
                if account:
                        flash('Conta já existe!')
                elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                        flash('Endereço de e-mail invalido')
                elif not re.match(r'[A-Za-z0-9]+', key):
                        flash('A senha deve conter apenas caracteres e números')
                elif not nome or not key or not email:
                        flash('Usuário, favor preenche os dados')
                else:
                        _hash_key = generate_password_hash(key)
                        cursor.execute = ("INSERT INTO users(nome, email, key) VALUES (%s, %s, %s)", (nome, email, _hash_key))
                        conn.commit()
                        flash('Registro cadastrado com Sucesso')
        elif request.method == 'POST':
                flash('Preencher os valores do formulário')
        return render_template('login.html')

@app.route('/logout/')
# Implementar o sair da aplicação




if __name__ == "__main__":
        app.run(debug=True)