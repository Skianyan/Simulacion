#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ejemplo para validar una contraseña encriptada con Python
#
# Ricardo Haro Calvo
# 06/03/2023
# ricardo.AT.haroware.DOT.com
#
import sqlite3
from flask import Flask, url_for, render_template, request

from Paginaweb.acceso import Contra

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/')
def index():
    url_for('index', filename="style.css")
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        # Conectar a BD
        conn = get_db_connection()
        # Encriptacion de contraseña
        activar = Contra(request.form['typeUser'],request.form['typePassword'])
        contrasenia = activar.encriptar
        existe = conn.execute(
                            "SELECT * FROM users WHERE correo=?",
                               (request.form['typeUser'],)
                              ).fetchone()
        if existe is not None:
            # Verificar si existe el password en tabla
            qry_data = conn.execute(
                "SELECT * FROM usuarios WHERE correo=? AND contra=?",
                (request.form['typeUser'],contrasenia,)
            ).fetchone()
            if qry_data is not None:
                error = "bienvenido"
            else:
                error = "existe un error con la contraseña"
        else:
            error = "Favor de registrarse"
        return render_template('acceso.html', error=error)