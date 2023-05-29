from models import db, user, pokemon, type as tipo_pokemon
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://joao:joao123@127.0.0.1:3306/PokemonSite'
db.init_app(app)

tipos = ["Normal","Fire","Water","Grass","Flying","Fighting","Poison","Electric","Ground","Rock","Psychic","Ice","Bug","Ghost","Steel","Dragon","Dark","Fairy"]
new_type = pokemon(PokemonName='testasfoda',PokemonImage='./static/Imagens/testasfoda.png')
with app.app_context():
    new_type.type.extend([db.session.get(tipo_pokemon, 1), db.session.get(tipo_pokemon, 12)])
    db.session.add(new_type)
    db.session.commit()