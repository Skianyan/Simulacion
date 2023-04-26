#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Encriptador en base 18
#
# Ricardo Haro Calvo
# Marzo 13, 2023
# ricardo.AT.haroware.DOT.com
#
import numpy

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
        self.geometry("270x140")
        self.title("Tarjetas de Crédito")
        # Inicializa la información
        self.contra = tk.StringVar()  # Palabra a encriptar
        self.encript = tk.StringVar()  # Palabra encriptada
        # Crear widget
        self.crear_widgets()

    def crear_widgets(self):
        datos = Frame(self, background='gray', relief=SUNKEN)
        datos.pack(fill=tk.X)
        # LABEL Y TEXTBOX Contrasenia
        ttk.Label(datos, text="Contra", justify=LEFT).pack(anchor=tk.W,
                                                           padx=10, pady=5, fill=tk.X)
        contra = Entry(datos, textvariable=self.contra)
        contra.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Button(datos, text="Encriptar", command=lambda: self.simula()).pack(side=tk.LEFT, padx=10)
        ttk.Button(datos, text="Salir", command=lambda: self.quit()).pack(side=tk.LEFT)
        # aquí se visualizará la solución
        resultados = Frame(self, background="blue")
        resultados.pack(fill=tk.X)

        ttk.Label(resultados, text="Encriptada", justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        encript = Entry(resultados, textvariable=self.encript)
        encript.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
    def simula(self):
        if not self.contra.get():
            messagebox.showerror('Error', 'Se debe indicar la palabra a encriptar')
            sys.exit(2)
        else:
            texto = self.contra.get()
            self.contra.set(texto)
        semilla = self.contabiliza()  #(Metodo para suma de vocales)

        # Random number Generator
        t = 164976
        a = 630360016  # Valor estatico
        # print('a= ' + str(a))
        m = (pow(2, 31)) - 1  # lo pide el problema
        # print('m= ' + str(m))
        multRndWithChar = []
        numAleatorio = []
        X = semilla
        i = 0
        while i < len(self.contra.get()):
            numAleatorio.insert(i, ((a * int(X)) % m))
            X = np.array(numAleatorio[i])
            Y = ord(self.contra.get()[i])
            print("Random number " + str(i) + ": " + str(X))
            print("Unicode " + str(i) + ": " + str(Y))
            multRndWithChar.insert(i,(np.ceil(X*Y)))
            i += 1

        print("mult RND * Unicode: "+ str(multRndWithChar))
        dividedmod = np.ceil([x / m for x in multRndWithChar])
        print (dividedmod)
        #output = "".join(str(i) for i in multRndWithChar)
        output = np.sum(multRndWithChar)
        print(output)
        #print(len(self.contra.get()))
        #print(self.contra.get()[0])
        #print(semilla)

        solution = np.base_repr(int(output), base=18)
        print(solution)

        palabra = "wadsf"
        print(palabra[-3:])
        # Mostrar soluciones
        self.encript.set(solution)

    def contabiliza(self):
        seedVoc = 0
        seedCons = 0
        seed = 0
        vocales = ('A', 'Á', 'À', 'E', 'É', 'È', 'I', 'Í', 'Ì', 'O', 'Ó', 'Ò', 'U', 'Ú', 'Ù','a','e','i','o','u','á','é','í','ó','ú')
        consonantes = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z',
                       'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z','!','@','#','$')
        for caracter in self.contra.get():
            if caracter in vocales:
                seedVoc += ord(caracter)
            if caracter in consonantes:
                seedCons += ord(caracter)
            seed = seedVoc * seedCons
        return seed


if __name__ == '__main__':
    app = App()
    app.mainloop()
