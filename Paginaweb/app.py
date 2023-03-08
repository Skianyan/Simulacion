#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ejemplo para validar una contraseña encriptada con Python
#
# Ricardo Haro Calvo
# 06/03/2023
# ricardo.AT.haroware.DOT.com
#
from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    url_for('index', filename="style.css")
    return render_template("index.html")

@app.route('/login')
def login():
    print('hehoo')