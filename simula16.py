#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ejemplo de Enfriamiento
# De una barra de metal
#
# Ricardo Haro Calvo
# Mayo 15, 2023
# ricardo.AT.haroware.DOT.com
#
import matplotlib.pyplot as plt

import math
from scipy import stats
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from metodos import rk4

class App():
    def __init__(self, root):
        self.root = root
        root.title("Enfriamiento") #Titulo
        root.geometry("450x300") #dimensiones
        #Inicializa la informacion
        self.TiempoInicial = tk.IntVar()    # Tiempo Inicial
        self.TempInicial = tk.IntVar()      # Temperatura Inicial
        self.TiempoFinal = tk.IntVar()      # Tiempo Final
        self.TempFinal = tk.IntVar()        # Temperatura Final
        self.TempAmbiente = tk.IntVar()     # Temperatura del Medio Ambiente
        #Crear los campos
        self.crear_widgets()
    def crear_widgets(self):
        #Se crea el frame para requerir informacion
        datos = Frame(self.root, height=2, bd=1, relief=SUNKEN) #widget properties
        datos.pack(fill=X, padx=10, pady=5)

        #Captura de velocidad del avion
        ttk.Label(datos, text="Tiempo Inicial", justify=CENTER).pack(fill=BOTH, expand=TRUE)
        tiempo_inicial = Entry(datos, textvariable=self.TiempoInicial, width=16)
        tiempo_inicial.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Temperatura Inicial", justify=CENTER).pack(fill=BOTH, expand=TRUE)
        temp_inicial = Entry(datos, textvariable=self.TempInicial, width=16)
        temp_inicial.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Tiempo Final", justify=CENTER).pack(fill=BOTH, expand=TRUE)
        tiempo_final = Entry(datos, textvariable=self.TiempoFinal, width=16)
        tiempo_final.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Temperatura Final", justify=CENTER).pack(fill=BOTH, expand=TRUE)
        temp_final = Entry(datos, textvariable=self.TempFinal, width=16)
        temp_final.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Temperatura Ambiente", justify=CENTER).pack(fill=BOTH, expand=TRUE)
        temp_ambiente = Entry(datos, textvariable=self.TempAmbiente, width=16)
        temp_ambiente.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        # Se crea un frame para los botones
        botones = Frame(self.root, height=2, bd=1, relief=SUNKEN)
        botones.pack(fill=X, padx=10, pady=5)
        ttk.Button(botones, text="Simular", command=lambda:self.simular()).pack(side=LEFT, padx=10, pady=5)
        ttk.Button(botones, text="Salir", command=lambda:self.root.quit()).pack(side=LEFT, padx=10, pady=5)

    def parametro(self):
        x=[]
        y=[]
        x0=int(self.TiempoInicial.get())
        x1=int(self.TiempoFinal.get())
        y0=int(self.TempInicial.get())
        y1=int(self.TempFinal.get())
        x.append(x0)
        x.append(x1)
        y.append(math.log(y0))
        y.append(math.log(y1))
        slope, intercept, rvalue, p_value, std_err = stats.linregress(x, y)
        return slope

    def resolver(self):
        x0 = int(self.TiempoInicial.get())
        x1 = int(self.TiempoFinal.get())
        y0 = int(self.TempInicial.get())
        y1 = int(self.TempFinal.get())
        vx, vy = rk4(self.funcion, x0, y0, 50, 100)
        plt.plot(vx, vy)
        plt.show()
    def funcion(self, x=None, y=None):
        k = self.parametro()
        TA = int(self.TempAmbiente.get())
        return k*(y-TA)
    def simular(self):
        #if self.verificar() == 5:
        self.resolver()
def main():
    root = Tk()
    App(root)  # aplicacion visual, normalmente definida como app
    root.mainloop()  # para mantener en pantalla

if __name__ == '__main__':
    main()