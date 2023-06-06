from control.POSTPokemon import SalvarPokemon
from flask import Flask, render_template, jsonify, request, send_file, url_for, redirect
from forms import CadastroPokemon
from models import db, type, pokemon as poke, pokemon_special
import json
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://aluno:aluno123@127.0.0.1:3306/pokemonsite'
app.config['SECRET_KEY'] = 'top10senhasfodas'
app.config['UPLOAD_FOLDER'] = './static/Imagens'

db.init_app(app)

def Load_Jsons(arquivo):
    with open(arquivo,'r') as f:
        return json.load(f)

pokemons_path = './JSonFiles/pokemons.json'

@app.route('/')
def index():
    return render_template('index.html', title = "index")

@app.route('/pokemon')
def pokemon():
    return render_template('foda.html', title = "pokemon")

@app.route('/criar_pokemon', methods=['GET', 'POST'])
def criar_pokemon():
    form = CadastroPokemon()
    form.tipo.choices = [(tipo.TypeID, tipo.TypeDescription) for tipo in type.query.all()]
    if request.method == 'POST':
        SalvarPokemon(repr(form))
        return redirect(url_for('index'))
    
    return render_template('criacao.html', title='Criação',form=form)

@app.route('/pokemon_data')
def pokemon_data():
    pokemons = poke.query.all()
    pokemon_data = {
        'pokemons': [
            {
                'id': pokemon.PokemonID,
                'name': pokemon.PokemonName,
                'Imagem': pokemon.PokemonImage,
                # 'tipos': pokemon.type
            }
            for pokemon in pokemons
        ]
    }
    print(pokemon_data)
    return jsonify(pokemon_data)

@app.route('/pokemon_data/<id>')
def pokemon_data_item(id):
    pokemon = db.session.get(poke, id)
    pokemon_data = {
        'id'    : pokemon.PokemonID,
        'name'  : pokemon.PokemonName,
        'imagem': pokemon.PokemonImage,
        'tipos':[
            tipo.TypeDescription
            for tipo in pokemon.type
        ]
    }
    return jsonify(pokemon_item=pokemon_data)

@app.route('/pokemon_special_data')
def pokemon_special_data():
    pokemon_specials = pokemon_special.query.all()
    pokemon_special_data = {
        'pokemons': [
            {
                'id': pokemon_special.Pokemon_specialID,
                'Classificacao': pokemon_special.Pokemon_specialTipo
            }
            for pokemon_special in pokemon_specials
        ]
    }
    return jsonify(pokemon_special_data)
            
if __name__ == '__main__':
    app.run(debug=True)
