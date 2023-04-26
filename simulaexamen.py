#!/usr/bin/python3
# -*-coding: utf-8 -*-
#
# Generador de tarjetas de crédito
#
# Ricardo H.C.
# Mar 13, 2023
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
        s = ttk.Style()
        s.theme_use('winnative')
        self.geometry("270x380")
        self.title("Tarjeta de crédito")
        # Inicializa la información
        self.appat = tk.StringVar() # Apellido Paterno
        self.apmat = tk.StringVar() # Apellido Materno
        self.nombre = tk.StringVar() # Nombre(s)
        self.vigencia = tk.StringVar() # Fecha de vigencia de la tarjeta
        self.cvv = tk.StringVar() # Código de validación
        self.tarjeta = tk.StringVar() # Tarjeta para el cliente
        # Crear widgets
        self.crear_widgets()
    def crear_widgets(self):
        datos = Frame(self, relief=SUNKEN)
        datos.pack(fill=tk.X)
        ttk.Label(datos, text="Nombre", justify=LEFT, background='#856ff8').pack(
            anchor=tk.W, padx=10, pady=5, fill=tk.X
        )
        nombre = Entry(datos, textvariable=self.nombre)
        nombre.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(datos, text="Primer apellido", justify=LEFT, background='#856ff8').pack(
            anchor=tk.W, padx=10, pady=5, fill=tk.X
        )
        appat = Entry(datos, textvariable=self.appat)
        appat.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(datos, text="Segundo apellido", justify=LEFT, background='#856ff8').pack(
            anchor=tk.W, padx=10, pady=5, fill=tk.X
        )
        apmat = Entry(datos, textvariable=self.apmat)
        apmat.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Button(datos, text="Crear cuenta", command=lambda: self.simula()).pack(side=tk.LEFT, padx=10, pady=5)
        ttk.Button(datos, text="Salir", command=lambda: self.quit()).pack(side=tk.LEFT, padx=10, pady=5)
        # Aquí se visualizará la solución
        resultados = Frame(self, relief=SUNKEN)
        resultados.pack(fill=tk.X)
        ttk.Label(resultados, text="Fecha de vigencia", background='#856ff8', justify=LEFT).pack(
            anchor=tk.W, padx=10, pady=5, fill=tk.X
        )
        vigencia = Entry(resultados, textvariable=self.vigencia)
        vigencia.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(resultados, text="CVV", background='#856ff8', justify=LEFT).pack(
            anchor=tk.W, padx=10, pady=5, fill=tk.X
        )
        cvv = Entry(resultados, textvariable=self.cvv)
        cvv.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(resultados, text="Tarjeta de crédito", background='#856ff8', justify=LEFT).pack(
            anchor=tk.W, padx=10, pady=5, fill=tk.X
        )

        tarjeta = Entry(resultados, textvariable=self.tarjeta)
        tarjeta.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
    def contabiliza(self):
        suma = 0
        vocales = ('A', 'Á', 'À', 'E', 'É', 'È', 'I', 'Í', 'Ì', 'O', 'Ó', 'Ò', 'U', 'Ú', 'Ù')
        nombre_persona = self.nombre.get() + self.appat.get() + self.apmat.get()
        for caracter in nombre_persona:
            if caracter in vocales:
                suma += ord(caracter)
        return suma
    @staticmethod
    def datos_tarjeta(semilla):
        t = 164976
        bandera = -1
        m = (2 ** 31) - 1
        a = 630360016
        x = [semilla]
        for i in range(1, 10):
            n = (a * x[i - 1]) % m
            x.append(n)
        for j in range(len(x)):
            # Convertir a texto
            dato = str(x[j])
            # Se extraen los cuatro primeros caracteres
            x[j] = dato[:4]
        return x
    def simula(self):
        if not self.appat.get():
            texto = 'X'
            self.appat.set(texto)
        else:
            texto = self.appat.get().upper()
            self.appat.set(texto)
        if not self.apmat.get():
            messagebox.showerror('Error', 'Se debe indicar el apellido materno de la persona')
            sys.exit(2)
        else:
            texto = self.apmat.get().upper()
            self.apmat.set(texto)
        if not self.nombre.get():
            messagebox.showerror('Error', 'Se debe indicar el nombre de la persona')
            sys.exit(2)
        else:
            texto = self.nombre.get().upper()
            self.nombre.set(texto)
            suma_vocales = self.contabiliza()
            print(suma_vocales)
            print(ord("A"))
            meses_num = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
            meses = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo',
            'Junio', 'Julio', 'Agosto', 'Septiembre',
            'Octubre', 'Noviembre', 'Diciembre'])
            indices_al_azar = np.random.permutation(len(meses_num))
            meses_num = meses_num[indices_al_azar]
            meses = meses[indices_al_azar]
            # Fecha de vigencia
            hoy = date.today()
            anio_vigencia = hoy.year + 3
            vigencia = meses[0] + '/' + str(anio_vigencia)
            # CVV
            valor_total = suma_vocales * anio_vigencia * meses_num[0]
            cv1 = str(valor_total)
            cv = cv1[-3:]
            # Se obtienen los valores para la tarjeta
            semilla = int(cv)
            valores_tarjeta = self.datos_tarjeta(semilla)
            digito2 = int(cv1[0])
            digito3 = int(cv1[1])
            digito4 = int(cv1[2])
            # Campos
            campo1 = '5' + cv1[:3]
            campo2 = valores_tarjeta[digito2] if len(valores_tarjeta[digito2]) == 4 else valores_tarjeta[digito2] + '0'

            campo3 = valores_tarjeta[digito3] if len(valores_tarjeta[digito3]) == 4 else valores_tarjeta[digito3] + '0'
            campo4 = valores_tarjeta[digito4] if len(valores_tarjeta[digito4]) == 4 else valores_tarjeta[digito4] + '0'
            tarjeta = campo1 + '-' + campo2 + '-' + campo3 + '-' + campo4
            # Mostrar soluciones
            self.vigencia.set(vigencia)
            self.cvv.set(cv)
            self.tarjeta.set(tarjeta)

if __name__ == '__main__':
   app = App()
   app.mainloop()