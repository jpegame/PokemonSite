from flask import Flask, render_template, jsonify, request, send_file, url_for, redirect
from forms import CadastroPokemon
import os
import json

def Load_Jsons(arquivo):
    with open(arquivo,'r') as f:
        return json.load(f)
app = Flask(__name__)
pokemons_path = './JSonFiles/pokemons.json'

app.config['SECRET_KEY'] = 'top10senhasfodas'
app.config['UPLOAD_FOLDER'] = './static/Imagens'

@app.route('/')
def index():
    return render_template('index.html', title = "index")

@app.route('/pokemon')
def pokemon():
    return render_template('foda.html', title = "pokemon")

@app.route('/criar_pokemon', methods=['GET', 'POST'])
def criar_pokemon():
    form = CadastroPokemon()
    if form.validate_on_submit():
        pokemons = Load_Jsons(pokemons_path)
        pokemon_solo = {
            "id"  : len(pokemons['pokemons']) + 1,
            "name": form.nome.data,
            "Base64": form.imagem.data,
            "types": form.tipo.data
        }
        pokemons['pokemons'].append(pokemon_solo)
        with open(pokemons_path,'w') as f:
            f.write(json.dumps(pokemons, indent=4))
    
    return render_template('criacao.html', title='Criação',form=form)

if __name__ == '__main__':
    app.run(debug=True)
