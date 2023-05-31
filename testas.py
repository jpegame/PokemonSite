from models import db, user, pokemon, type as tipo_pokemon
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://uvvp03qrxb766qoc:HcvkJP3kEvL4bJCkZ0TY@bgbgdk5d0uglfiuiprtq-mysql.services.clever-cloud.com:3306/bgbgdk5d0uglfiuiprtq'
db.init_app(app)

# tipos = ["Normal","Fire","Water","Grass","Flying","Fighting","Poison","Electric","Ground","Rock","Psychic","Ice","Bug","Ghost","Steel","Dragon","Dark","Fairy"]
# new_type = pokemon(PokemonName='testasfoda',PokemonImage='./static/Imagens/testasfoda.png')
# for tipo in tipos:
#     with app.app_context():
#         new_type = tipo_pokemon(TypeDescription=tipo)
#         db.session.add(new_type)
#         db.session.commit()

with open('./JSonFiles/pokemons.json','r') as f:
    pokemonjson = json.load(f)
    