#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Encriptador en base 18
#
# Ricardo Haro Calvo
# Marzo 13, 2023
# ricardo.AT.haroware.DOT.com
#
import random

import math
import sys
from datetime import date
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import numpy as np


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("270x200")
        self.title("Tarjetas de Crédito")
        # Inicializa la información
        self.vigencia = tk.StringVar()  # Fecha de vigencia de la tarjeta
        self.ccv = tk.StringVar()  # Código de validación
        self.tarjeta = tk.StringVar()  # Tarjeta para el cliente
        # Crear widget
        self.crear_widgets()

    def crear_widgets(self):
        datos = Frame(self, background='gray', relief=SUNKEN)
        datos.pack(fill=tk.X)
        # LABEL Y TEXTBOX NOMBRE

        ttk.Button(datos, text="Crear cuenta", command=lambda: self.simula()).pack(side=tk.LEFT, padx=10)
        ttk.Button(datos, text="Salir", command=lambda: self.quit()).pack(side=tk.LEFT)
        # aquí se visualizará la solución
        resultados = Frame(self, background="blue")
        resultados.pack(fill=tk.X)

        ttk.Label(resultados, text="Fecha de vigencia", justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        vigencia = Entry(resultados, textvariable=self.vigencia)
        vigencia.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(resultados, text="CVV", justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ccv = Entry(resultados, textvariable=self.ccv)
        ccv.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(resultados, text="Tarjeta", justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        tarjeta = Entry(resultados, textvariable=self.tarjeta)
        tarjeta.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
    def simula(self):
        ## Problema dice Noviembre 2023, 15H27M
        semilla = (2026 * 11)   #(Metodo para suma de vocales)
        semilla = (2025 * 8 * 16 * 21)    # SEMILLA DE EJEMPLO, COMENTAR
        cv1 = str(semilla)
        cvv = cv1[:3]
        cvv = 200               # CVV DE EJEMPLO, COMENTAR
        print("Semilla: " + str(semilla))
        print("CVV: " + str(cvv))

        # 1.- **** .... .... ....
        # Random number Generator
        t = 14348910        # Set por el problema (REAL)
        t = 14348907        # Set por el problema (EJEMPLO, COMENTAR DESPUES)
        a = (8 * t) - 3     # Valor estatico
        m = pow(2, 32)      # Lo pide asi el problema
                            # Printmethod: # print('m= ' + str(m))

        num1 = random.randint(5001,5998)
        print("RNG num: " + str(num1))
        ##### HARDCODED POR EL PROBLEMA #####
        num1
        num1 = (a * cvv % m) / m
        print(num1)

        # 2.- .... **** .... ....
        hold = str(num1)
        seedfor2 = hold[-3:]
        print("semilla 2: " + seedfor2)


        form2 = []
        X = seedfor2
        i = 0
        #while i < cvv:
        #    form2.insert((i, ((a * int(X)) % m)) / m)
        #    X = form2[i]
        #    i += 1
        #print(form2)

        hold = str(X)
        num2 = hold[-4:]
        print("numero 2: " + str(num2))

        # 3.- .... .... **** ....
        form3 = []
        X = hold[-3:]
        print("semilla3:" + X)
        X = int(X)
        i = 0
        while i < X:
            form3.insert(i, ((a * int(X)) % m))
            X = form3[i] / m
            i += 1
        print(X)


        # 4.- .... .... .... ****


        # Mostrar soluciones
        self.vigencia.set("2026")
        self.ccv.set(cvv)
        self.tarjeta.set(str(num1) + " " + str(num2))

    def contabiliza(self):
        return 0


if __name__ == '__main__':
    app = App()
    app.mainloop()
