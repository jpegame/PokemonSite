from flask import Flask, render_template, jsonify, request, send_file, url_for, redirect
from forms import CadastroPokemon
import os
import json
import base64

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
            "Imagem": './static/Imagens/'+ form.nome.data + '.png',
            "types": form.tipo.data
        }
        pokemons['pokemons'].append(pokemon_solo)
        with open(pokemons_path,'w') as f:
            f.write(json.dumps(pokemons, indent=4))
        base64_to_image(form.imagem.data, './static/Imagens/'+ form.nome.data + '.png')
        return redirect(url_for('index'))
    
    return render_template('criacao.html', title='Criação',form=form)


def base64_to_image(base64_string, output_path):
    base64_data = base64_string.split(',')[1]
    image_data = base64.b64decode(base64_data)

    with open(output_path, 'wb') as f:
        f.write(image_data)

@app.route('/pokemon_data')
def pokemon_data():
    return send_file(pokemons_path, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
