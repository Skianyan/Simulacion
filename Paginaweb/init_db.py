#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Clase para iniciar la base de datos
#
# Ricardo Haro Calvo
# 07 Marzo, 2023
# ricardo.AT.haroware.DOT.com
#

import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO usuarios(nombre, correo, contra) VALUES (?,?,?)"),
            ('Juan Perez', 'jperez@ite.edu.mx', '11CC6B632C292D')