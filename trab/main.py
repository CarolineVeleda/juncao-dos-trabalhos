#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import app
from flask import Blueprint
from flask import redirect, url_for
from app.controllers.home_bp import home_bp
from app.controllers.printer_bp import printer_bp
from flask_bootstrap import Bootstrap
from flask_babel import Babel
from flask import Flask, render_template, request
from form import Formulario


app = Flask(__name__)
app.secret_key = 'development key'

app.config["BABEL_DEFAULT_LOCALE"] = "pt"
babel = Babel(app)

app.register_blueprint(home_bp)
app.register_blueprint(printer_bp)

@app.route('/')
def index():
    return redirect(home_bp.url_prefix)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run('0.0.0.0', port=port)


