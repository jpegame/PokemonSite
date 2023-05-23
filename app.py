from flask import Flask, render_template, jsonify, request, send_file, url_for, redirect
from forms import CadastroPokemon
import os
import json

app = Flask(__name__)
file_path = './JSONFiles/mercadinho.json'
carrinho_path = './JSONFiles/carrinho.json'

app.config['SECRET_KEY'] = 'top10senhasfodas'
app.config['UPLOAD_FOLDER'] = './static/Imagens'

@app.route('/')
def index():
    return render_template('index.html', title = "index")

@app.route('/pokemon')
def pokemon():
    return render_template('foda.html', title = "pokemon")

@app.route('/criar_pokemon')
def criar_pokemon():
    return render_template('criacao.html', title='Criação')

if __name__ == '__main__':
    app.run(debug=True)
