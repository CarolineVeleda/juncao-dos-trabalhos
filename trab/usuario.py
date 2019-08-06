from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.widgets.html5 import NumberInput
from wtforms import IntegerField
import psycopg2


class Usuario:
    def __init__(self,nome,login, altura, idade, email, senha):
        self._nome = nome
        self._login = login
        self._altura = altura
        self._idade = idade
        self._email = email
        self._senha = senha

    def _get_nome(self):
        return self._nome
    
    def _get_email(self):
        return self._email

    def _get_cod(self):
        return self._cod
    
    def _get_login(self):
        return self._login
    
    def _get_senha(self):
        return self._senha
    
    def altura(self):
        return self._altura
    
    def idade(self):
        return self._idade
    
    def _set_nome(self, nome):
        self._nome = nome
    
    def _set_email(self, email):
        self._email = email
    
    def _set_cod(self, cod):
        self._cod = cod
    
    def _set_login(self,login):
        self._login = login
    
    def _set_senha(self,senha):
        self._senha = senha
    
    def _set_senha(self,altura):
        self._altura = altura

    def _set_idade(self,idade):
        self._idade = idade
    

    nome = property(_get_nome,_set_nome)
    email = property(_get_email,_set_email)
    cod = property(_get_cod,_set_cod)
    altura = property(_get_altura,_set_altura)
    login = property(_get_login,_set_login)
    senha = property(_get_senha,_set_senha)
    idade = property(_get_idade,_set_idade)



'''
class Usuario(Form):
    nome = StringField('Nome',validators=[DataRequired()])
    login = StringField('Login',validators=[DataRequired()])
    altura = IntegerField('Altura', validators=[DataRequired()],widget=NumberInput(max=4))
    idade = IntegerField('Altura', validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired()])
    senha = StringField('Senha',validators=[DataRequired()])
    enviar = SubmitField("Enviar")
    '''