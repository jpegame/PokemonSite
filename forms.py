from http.client import PRECONDITION_FAILED
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, FileField, SelectMultipleField
#from wtforms.fields import CanvasField
from wtforms.validators import DataRequired

#tipos = ["Normal","Fire","Water","Grass","Flying","Fighting","Poison","Electric","Ground","Rock","Psychic","Ice","Bug","Ghost","Steel","Dragon","Dark","Fairy"]

class CadastroPokemon(FlaskForm):
    tipo = SelectMultipleField('Tipo', validators=[DataRequired()], default = "", choices=[])
    nome = StringField('Nome', validators=[DataRequired()])
    imagem  =StringField('imagem', validators=[DataRequired()])
    submit = SubmitField('Manda ae paizao')