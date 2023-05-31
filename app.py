from control.POSTPokemon import SalvarPokemon
from flask import Flask, render_template, jsonify, request, send_file, url_for, redirect
from forms import CadastroPokemon
from models import db, type, pokemon as poke
import json
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://uvvp03qrxb766qoc:HcvkJP3kEvL4bJCkZ0TY@bgbgdk5d0uglfiuiprtq-mysql.services.clever-cloud.com:3306/bgbgdk5d0uglfiuiprtq'
app.config['SECRET_KEY'] = 'top10senhasfodas'
app.config['UPLOAD_FOLDER'] = './static/Imagens'

db.init_app(app)

def Load_Jsons(arquivo):
    with open(arquivo,'r') as f:
        return json.load(f)

def base64_to_image(base64_string, output_path):
    base64_data = base64_string.split(',')[1]
    image_data = base64.b64decode(base64_data)

    with open(output_path, 'wb') as f:
        f.write(image_data)

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
        # pokemons = Load_Jsons(pokemons_path)
        # pokemon_solo = {
        #     "id"  : len(pokemons['pokemons']) + 1,
        #     "name": form.nome.data,
        #     "Imagem": './static/Imagens/'+ form.nome.data + '.png',
        #     "types": form.tipo.data
        # }
        # pokemons['pokemons'].append(pokemon_solo)
        # with open(pokemons_path,'w') as f:
        #     f.write(json.dumps(pokemons, indent=4))
        # base64_to_image(form.imagem.data, './static/Imagens/'+ form.nome.data + '.png')
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
                'Imagem': pokemon.PokemonImage
            }
            for pokemon in pokemons
        ]
    }
    return jsonify(pokemon_data)

@app.route('/pokemon_data/<id>')
def pokemon_data_item(id):
    pokemons = Load_Jsons(pokemons_path)
    for pokemon_item in pokemons['pokemons']:
        if pokemon_item['id'] == int(id):
            return jsonify(pokemon_item=pokemon_item)
            

if __name__ == '__main__':
    app.run(debug=True)
