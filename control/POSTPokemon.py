from models import db, type as tipoclass, pokemon
from flask import Flask
import json
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://uvvp03qrxb766qoc:HcvkJP3kEvL4bJCkZ0TY@bgbgdk5d0uglfiuiprtq-mysql.services.clever-cloud.com:3306/bgbgdk5d0uglfiuiprtq'
db.init_app(app)

class SalvarPokemon():
    def __init__(self, PokemonJson):
        PokemonDict = json.loads(PokemonJson)
        with app.app_context():
            TipoPokemon = [db.session.get(tipoclass, TipoID) for TipoID in PokemonDict['tipos']]
            Pokemon = pokemon(PokemonName=PokemonDict['nome'],PokemonImage='../static/Imagens/'+ PokemonDict['nome'] + '.png')
            Pokemon.type.extend(TipoPokemon)
            db.session.add(Pokemon)
            db.session.commit()
        self.base64_to_image(PokemonDict['imagem'], '../static/Imagens/'+ PokemonDict['nome'] + '.png')

    def base64_to_image(self,base64_string, output_path):
        base64_data = base64_string.split(',')[1]
        image_data = base64.b64decode(base64_data)

        with open(output_path, 'wb') as f:
            f.write(image_data)