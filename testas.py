# from models import db, user, pokemon, type as tipo_pokemon
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import json

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://uvvp03qrxb766qoc:HcvkJP3kEvL4bJCkZ0TY@bgbgdk5d0uglfiuiprtq-mysql.services.clever-cloud.com:3306/bgbgdk5d0uglfiuiprtq'
# db.init_app(app)

# tipos = ["Normal","Fire","Water","Grass","Flying","Fighting","Poison","Electric","Ground","Rock","Psychic","Ice","Bug","Ghost","Steel","Dragon","Dark","Fairy"]
# new_type = pokemon(PokemonName='testasfoda',PokemonImage='./static/Imagens/testasfoda.png')
# for tipo in tipos:
#     with app.app_context():
#         new_type = tipo_pokemon(TypeDescription=tipo)
#         db.session.add(new_type)
#         db.session.commit()

# with open('./JSonFiles/pokemons.json','r') as f:
#     pokemonjson = json.load(f)
# import json
# import requests

# for i in range(1,810):
#     r = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(i))
#     JsonData = json.loads(r.content)
#     if JsonData['is_mythical'] == True:
#         print(f"{i}||{JsonData['name']}|| M")
#     if JsonData['is_legendary'] == True:
#         print(f"{i} || {JsonData['name']}|| L")
from models import db, user, pokemon, type as tipo_pokemon, pokemon_special
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://joao:joao123@127.0.0.1:3306/pokemonsite'
db.init_app(app)


f = open('testas.txt','r')
lista = f.readlines()
for l in lista:
    l = l.replace("\n","")
    pokemon_lista = l.split('||')

    with app.app_context():
        new_type = pokemon_special(Pokemon_specialID=int(pokemon_lista[0]),Pokemon_specialTipo=pokemon_lista[2].replace(" ", ""))
        db.session.add(new_type)
        db.session.commit()