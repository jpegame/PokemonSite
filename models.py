from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(80), nullable=True, unique=True)
    UserEmail = db.Column(db.String(120), nullable=True, unique=True)

Pokemon_Type = db.Table('Pokemon_Type',
    db.Column('PokemonID', db.Integer, db.ForeignKey('pokemon.PokemonID'), primary_key=True),
    db.Column('TypeID', db.Integer, db.ForeignKey('type.TypeID'), primary_key=True)
)

class pokemon(db.Model):
    PokemonID = db.Column(db.Integer, primary_key=True)
    PokemonName = db.Column(db.String(60), nullable=True)
    PokemonImage = db.Column(db.String(100), nullable=True)
    type = db.relationship('type', secondary=Pokemon_Type, backref='pokemon')

class type(db.Model):
    TypeID = db.Column(db.Integer, primary_key=True)
    TypeDescription = db.Column(db.String(40), unique=True)

class pokemon_special(db.Model):
    Pokemon_specialID = db.Column(db.Integer, primary_key=True)
    Pokemon_specialTipo = db.Column(db.String(1))
