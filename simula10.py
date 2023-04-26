#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simulador de cálculo de probabilidad
# basandose en una distribucion normal
#
# Ricardo Haro Calvo
# Abril 19, 2023
# ricardo.AT.haroware.DOT.com
#

import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import numpy as np

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("310x450")
        self.title("Calculo de probablilidad")
        # Se inicializa la información
        self.media = tk.DoubleVar() # Promedio
        self.desvest = tk.DoubleVar() # Desviación Estándar
        self.valor_minimo = tk.DoubleVar() # Para el cálculo por si es por intervalo. Valor mínimo
        self.valor_maximo = tk.DoubleVar() # Para el cálculo por si es por intervalo. Valor máximo
        self.simulacion = tk.StringVar() # Tipo de problema a resolver <, <=, ...
        self.solucion = tk.DoubleVar() # Valor obtenido
        # Crear los campos
        self.crear_widgets()

    def crear_widgets(self):
        datos = Frame(self)
        datos.pack(fill=tk.X)
        ttk.Label(datos, text="Indique el promedio de los datos",
                  justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        media = Entry(datos, textvariable=self.media)
        media.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(datos, text="Indique la desviación estándar",
                  justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        desviacion = Entry(datos, textvariable=self.desvest)
        desviacion.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(datos, text="Tipo de cálculo a realizar",
                  justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        forma = ttk.Combobox(datos, textvariable=self.simulacion, state='readonly',
                             values=["<","<=",">",">=","a<=x<=b"])
        forma.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        forma.current()
        ttk.Label(datos, text="Valor mínimo del intervalo (cuando aplique)",
                  justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        minimo = Entry(datos, textvariable=self.valor_minimo)
        minimo.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(datos, text="Valor máximo del intervalo (cuando aplique)",
                  justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        maximo = Entry(datos, textvariable=self.valor_maximo)
        maximo.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Button(datos, text="Simular", command=lambda: self.calculo_probabilidad()).pack(side=tk.LEFT, padx=10, pady=5)
        ttk.Button(datos, text="Salir", command=lambda: self.quit()).pack(side=tk.LEFT, padx=10, pady=5)

        solucion = Frame(self)
        solucion.pack(fill=X)
        solucion.config(bg="gray")
        ttk.Label(solucion, text="Probabilidad estimada", justify= LEFT,
                  background="gray").pack(anchor=tk.W,padx=10,pady=5)
        probabilidad = Entry(solucion, textvariable=self.solucion)
        probabilidad.pack(anchor=tk.W,padx=10,pady=5,fill=tk.X)
    @staticmethod
    def lectura(combo):
        switch ={
            '<': 1,
            '<=': 2,
            '>': 3,
            '>=': 4,
            'a<=x<=b': 5
        }
        return switch.get(combo, 'e')
    def calculo_probabilidad(self):
        if not self.media.get():
            messagebox.showerror("Error de Media", "Se debe declarar el promedio de los datos")
            sys.exit(2)
        if not self.desvest.get():
            messagebox.showerror("Error de Desviacion estandar", "Se debe declarar la desviacion estandar de los datos")
            sys.exit(2)
        if self.desvest.get()<=0:
            messagebox.showerror("Valor incongruente", "La desviacion estandar debe ser un valor positivo")
            sys.exit(2)
        if self.simulacion.get():
            messagebox.showerror("Error de tipo de problema", "Debe indicar tipo de cálculo por realizar")
            sys.exit(2)
        suma = 0
        tipo_calculo = self.lectura(self.simulacion.get())
        #if tipo_calculo == 0:

        if tipo_calculo == 5:
            if not self.valor_minimo.get():
                messagebox.showerror("Falta valor a", "Debe indicar el valor mínimo del problema")
                sys.exit(2)
            if not self.valor_maximo.get():
                messagebox.showerror("Falta valor b", "Debe indicar el valor máximo del problema")
                sys.exit(2)
            if self.valor_minimo.get() >= self.valor_maximo.get():
                messagebox.showerror("Error de parametros",
                                     "El valor minimo es superior, no se puede realizar el calculo")
                sys.exit(2)
        else:
            if not self.valor_minimo.get():
                messagebox.showerror("Error de ingreso", "Debe declarar el valor por calcular")
                sys.exit(2)


if __name__ == '__main__':
    app = App()
    app.mainloop()