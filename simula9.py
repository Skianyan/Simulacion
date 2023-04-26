#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Generador de Tarjetas de Credito
#
# Ricardo Haro Calvo
# Marzo 13, 2023
# ricardo.AT.haroware.DOT.com
#

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
        self.geometry("270x380")
        self.title("Tarjetas de Crédito")
        # Inicializa la información
        self.appat = tk.StringVar()     # Apellido Paterno
        self.apmat = tk.StringVar()     # Apellido Materno
        self.nombre = tk.StringVar()    # Nombre
        self.vigencia = tk.StringVar()  # Fecha de vigencia de la tarjeta
        self.ccv =  tk.StringVar()      # Código de validación
        self.tarjeta = tk.StringVar()   # Tarjeta para el cliente
        # Crear widget
        self.crear_widgets()
    def crear_widgets(self):
        datos = Frame(self, background='gray', relief=SUNKEN)
        datos.pack(fill=tk.X)
        # LABEL Y TEXTBOX NOMBRE
        ttk.Label(datos, text="Nombre", justify=LEFT).pack(anchor=tk.W,
                                                           padx=10, pady=5, fill=tk.X)
        nombre = Entry(datos, textvariable=self.nombre)
        nombre.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        # LABEL Y TEXTBOX APPELLIDO PATERNO
        ttk.Label(datos, text="Apellido Paterno", justify=LEFT).pack(anchor=tk.W,
                                                                     padx=10, pady=5, fill=tk.X)
        appat = Entry(datos, textvariable=self.appat)
        appat.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        # LABEL Y TEXTBOX APPELLIDO MATERNO
        ttk.Label(datos, text="Apellido Materno", justify=LEFT).pack(anchor=tk.W,
                                                                     padx=10, pady=5, fill=tk.X)
        apmat = Entry(datos, textvariable=self.apmat)
        apmat.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Button(datos, text="Crear cuenta", command=lambda: self.simula()).pack(side=tk.LEFT,padx=10)
        ttk.Button(datos, text="Salir", command=lambda: self.quit()).pack(side=tk.LEFT)
        #aquí se visualizará la solución
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
        if not self.appat.get():
            texto = "X"
            self.appat.set(texto)
        else:
            texto = self.appat.get().upper()
            self.appat.set(texto)
        if not self.apmat.get():
            messagebox.showerror('Error','Se debe indicar el apellido materno de la persona')
            sys.exit(2)
        else:
            texto = self.apmat.get().upper()
            self.apmat.set(texto)
        if not self.nombre.get():
            messagebox.showerror('Error','Se debe indicar el nombre de la persona')
            sys.exit(2)
        else:
            texto = self.nombre.get().upper()
            self.nombre.set(texto)
        suma_vocales = self.contabiliza()
        meses_num = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        meses = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                          'Julio', 'Agosto','Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
        indices_al_azar = np.random.permutation(len(meses_num))
        meses_num = meses_num[indices_al_azar]
        meses = meses[indices_al_azar]

        #Fecha de vigencia
        hoy = date.today()
        anio_vigencia = hoy.year + 3
        vigencia = meses[0] + '/' + str(anio_vigencia)

        #CVV
        valor_total = suma_vocales * anio_vigencia * meses_num[0]
        cv1 = str(valor_total)
        cv = cv1[-3:]
        cvstr = str(cv)

        #Tarjeta (tarea, completar tarjeta aleatoria)
        # 1-4
        num_tarj1 = '5' + cv1[:3]

        # 5-8
        t = 164976
        a = (8 * t) + 3
        #print('a= ' + str(a))
        m = pow(2, 31)
        #print('m= ' + str(m))
        form = []
        X = 620
        i = 0
        while i < 9:
            form.insert(i, ((a * int(X)) % m))
            X = form[i]
            i += 1

        #print(cvstr[0])
        formnum2 = int(cvstr[0]) - 1
        num2=form[formnum2]
        num2str = str(num2)
        num_tarj2 = num2str[:4]

        # 9-12
        #print(cvstr[1])
        formnum3 = int(cvstr[1]) - 1
        num3 = form[formnum3]
        num3str = str(num3)
        num_tarj3 = num3str[:4]

        # 13-16
        #print(cvstr[2])
        formnum4 = int(cvstr[2]) - 1
        num4 = form[formnum4]
        num4str = str(num4)
        num_tarj4 = num4str[:4]

        # Mostrar soluciones
        self.vigencia.set(vigencia)
        self.ccv.set(cv)
        self.tarjeta.set(num_tarj1 + " - " + num_tarj2 + " - " + num_tarj3 + " - " + num_tarj4)

    def contabiliza(self):
        suma = 0
        vocales = ('A','Á','À','E','É','È','I','Í','Ì','O','Ó','Ò','U','Ú','Ù')
        nombre_persona = self.nombre.get() + self.appat.get() + self.apmat.get()
        for caracter in nombre_persona:
            if caracter in vocales:
                suma += ord(caracter)
        return suma

if __name__ == '__main__':
    app = App()
    app.mainloop()
    