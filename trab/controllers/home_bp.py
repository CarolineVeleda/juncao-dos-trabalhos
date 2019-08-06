# -*- coding: utf-8 -*-
from flask import Blueprint

home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/')
def index():
    return render_template('form.html')

'''
def index():
    form = Formulario()
    if form.validate_on_submit():
        return "Enviado com sucesso"
    return render_template('formulario.html',form=form,pessoa=pessoa)
'''

@app.route('/inserir', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,form.password.data)
        
        #db_session.add(user)
        flash('Thanks for registering')
        #return redirect(url_for('login'))
    return render_template('cadastro.html', form=form)







