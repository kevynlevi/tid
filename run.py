from flask import Flask, redirect, url_for, flash, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user
from datetime import datetime
import os
from sqlalchemy import Enum

app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# Defina a pasta onde os arquivos enviados serão armazenados
app.config['UPLOAD_FOLDER'] = 'uploads'

# Defina as extensões de arquivo permitidas para upload
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Models do banco de dados
class Cliente(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    placa = db.Column(db.String(7), nullable=False, unique=True)
    

class Empresa(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome_empresa = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    bairro = db.Column(db.String(255), nullable=False)
    cidade = db.Column(db.String(255), nullable=False)
    vagas = db.Column(db.Integer, nullable=False)
    tipo_preco = db.Column(Enum('Por hora', 'Diária'), nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    # Retorna o usuário com base no ID
    cliente = Cliente.query.get(int(user_id))
    if cliente:
        return cliente
    else:
        return Empresa.query.get(int(user_id))

@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/cliente.html')
def cliente_html():
    return render_template('cliente.html')
@app.route('/login.html')
def logar():
    return render_template('login.html')
@app.route('/empresa.html')
def empresa_html():
    return render_template('empresa.html')

@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        # Retrieve data from the form
        nome = request.form['event-nome']
        email = request.form['event-email']
        senha = request.form['event-senha']
        placa = request.form['plate-number']
        
        # Get the current logged-in user
        usuario_atual = current_user
        
        # Create a new Cliente instance and associate it with the current user
        new_cliente = Cliente(usuario=usuario_atual, nome=nome, email=email, senha=senha, placa=placa)
        
        # Add the new cliente to the database
        db.session.add(new_cliente)
        db.session.commit()
        
        return render_template("index.html")
    else:
        return 'Método não permitido!'

@app.route('/cadastrar_empresa', methods=['POST'])
def cadastrar_empresa():
    if request.method == 'POST':
        # Retrieve data from the form
        nome_empresa = request.form['company-name']
        email = request.form['email']
        senha = request.form['password']
        cep = request.form['cep']
        endereco = request.form['address']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        vagas = request.form['vacancies']
        tipo_preco = request.form['price-type']
        preco = request.form['money']
        
        # Check if the email already exists in the database
        existing_empresa = Empresa.query.filter_by(email=email).first()
        if existing_empresa:
            return 'Este email já está em uso!'
        
        # Create a new Empresa instance
        new_empresa = Empresa(nome_empresa=nome_empresa, email=email, senha=senha, cep=cep, endereco=endereco,
                              bairro=bairro, cidade=cidade, vagas=vagas, tipo_preco=tipo_preco, preco=preco)
        
        # Add the new empresa to the database
        db.session.add(new_empresa)
        db.session.commit()
        
        return redirect(url_for('index'))
    else:
        return 'Método não permitido!'

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['event-email']
        senha = request.form['event-senha']
        
        # Verifica se o usuário é um cliente
        cliente = Cliente.query.filter_by(email=email, senha=senha).first()
        if cliente:
            login_user(cliente)
            return render_template('pesqclnt.html')
        
        # Verifica se o usuário é uma empresa
        empresa = Empresa.query.filter_by(email=email, senha=senha).first()
        if empresa:
            login_user(empresa)
            return render_template('pesqemp.html')
        
        # Se nenhum usuário for encontrado, exibe uma mensagem de erro
        flash('Credenciais inválidas. Por favor, tente novamente.', 'error')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/empresa')
def empresa():
    if current_user.is_authenticated and isinstance(current_user, Empresa):
        return render_template('pesqemp.html')
    else:
        flash('Acesso não autorizado.', 'error')
        return redirect(url_for('index'))

@app.route('/cliente')
def cliente():
    if current_user.is_authenticated and isinstance(current_user, Cliente):
        return render_template('pesqclnt.html')
    else:
        flash('Acesso não autorizado.', 'error')
        return redirect(url_for('index'))

@app.route('/telafinal.html')
def telafinal():
    return render_template('telafinal.html')
@app.route('/pesquisar_carro', methods=['POST'])
def pesquisar_carro():
    if request.method == 'POST':
        # Obtenha a placa do carro da solicitação POST
        placa = request.form['event-nome']
        
        # Pesquise no banco de dados as informações do carro com base na placa
        carro = Cliente.query.filter_by(placa=placa).first()
        
        if carro:
            # Se o carro for encontrado, passe as informações para o template HTML
            return render_template("telafinalDois.html", carro=carro)
        else:
            # Se o carro não for encontrado, exiba uma mensagem de erro
            flash('Carro não encontrado.', 'error')
            return redirect(url_for('index'))
    else:
        return 'Método não permitido!'

if __name__ == "__main__":
    app.run(debug=True)
