#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ejemplo del infeccion
# Utilizando el metodo de Runge-Kutta
#
# Ricardo Haro Calvo
# Mayo 9, 2023
# ricardo.AT.haroware.DOT.com
#

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
        root.title("Infectados") #Titulo
        root.geometry("450x300") #dimensiones
        #Inicializa la informacion
        self.Poblacion = tk.IntVar() # Poblacion
        self.InfectInicio = tk.IntVar() # Personas Infectadas tiempo inicial
        self.TiempoFinal = tk.IntVar()  # Tiempo Final
        self.InfectFinal = tk.IntVar()  # Personas infectadas en el periodo
        #Crear los campos
        self.crear_widgets()

    def crear_widgets(self):
        #Se crea el frame para requerir informacion
        datos = Frame(self.root, height=2, bd=1, relief=SUNKEN) #widget properties
        datos.pack(fill=X, padx=10, pady=5)

        #Captura de velocidad del avion
        ttk.Label(datos, text="Poblacion", justify=LEFT).pack(fill=BOTH, expand=TRUE)
        poblacion = Entry(datos, textvariable=self.Poblacion, width=16)
        poblacion.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Infectados al inicio", justify=LEFT).pack(fill=BOTH, expand=TRUE)
        infect_inicio = Entry(datos, textvariable=self.InfectInicio, width=16)
        infect_inicio.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Tiempo Final", justify=LEFT).pack(fill=BOTH, expand=TRUE)
        tiempo_final = Entry(datos, textvariable=self.TiempoFinal, width=16)
        tiempo_final.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Infectados al final", justify=LEFT).pack(fill=BOTH, expand=TRUE)
        infect_final = Entry(datos, textvariable=self.InfectFinal, width=16)
        infect_final.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        # Se crea un frame para los botones
        botones = Frame(self.root, height=2, bd=1, relief=SUNKEN)
        botones.pack(fill=X, padx=10, pady=5)
        ttk.Button(botones, text="Graficar", command=lambda:self.simular()).pack(side=LEFT, padx=10, pady=5)
        ttk.Button(botones, text="Salir", command=lambda:self.root.quit()).pack(side=LEFT, padx=10, pady=5)

    def verificar(self):
        bandera = 0
        # Validacion de Poblacion
        if not self.Poblacion.get():
            messagebox.showerror("Error", "No se ha declarado la poblacion")
        else:
            if self.Poblacion.get() < 0:
                messagebox.showerror("Poblacion no validada", "No se puede declarar una poblacion negativa")
            else:
                bandera += 1

        # Validacion de Infectados Iniciales
        if not self.InfectInicio.get():
            messagebox.showerror("Error", "No se ha declarado los infectados iniciales")
        else:
            if self.InfectInicio.get() < 0:
                messagebox.showerror("Infectados no validados", "No se puede declarar cantidad de infectados negativos")
            else:
                bandera += 1

        # Validacion de Tiempo Final
        if not self.TiempoFinal.get():
            messagebox.showerror("Error","No se ha declarado el tiempo final")
        else:
            if self.TiempoFinal.get() < 0:
                messagebox.showerror("Velocidad no validada", "No se puede declarar tiempo final negativo")
            else:
                bandera += 1

        # Validacion de Infectados Finales
        if not self.InfectFinal.get():
            messagebox.showerror("Error","No se ha declarado los infectados finales")
        else:
            if self.InfectFinal.get() < 0:
                messagebox.showerror("Velocidad no validada", "No se puede declarar infectados finales negativos")
            else:
                bandera += 1
        return bandera


    def funcion(self, x=None, y=None):
        k = 5
        a = 32
        b = a/k
        return k * y * (a - b * y)

    def simular(self):
        if self.verificar() == 4:
            self.parametro()
            self.resolver()

    def resolver(self):
        #Primero, se crea un figura contenedora
        fig = Figure(figsize=(5, 5))
        vx,vy = rk4(self.funcion, self.x0, self.y0, self.x1, self.y1) #(0,0,1,1) 0 son las concidiones iniciales
        # 1 son las condiciones finales
        # Se crea una subfigura
        plot1 = fig.add_subplot(111)
        # Se grafica
        plot1.plot(vx, vy)
        # Se añade a Tkinter como un elemento Canvas
        canvas = FigureCanvasTkAgg(fig, self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, self.root)
        toolbar.update()
        canvas.get_tk_widget().pack()

    def parametro(self):
        # Se definen los parametros
        x0 = 0                                  #tiempo inicial
        x1 = self.TiempoFinal.get()             #tiempo final
        y0 = math.log(self.InfectInicio.get())  #infectados iniciales
        y1 = math.log(self.InfectFinal.get())   #infectados finales
        print(x0, x1, y0, y1)
        # Arreglos
        x = [0]
        x.append(x1)
        y = [y0]
        y.append(y1)

        slope, intercept, rvalue, p_value, std_err = stats.linregress(x, y)
        print (slope)
        return slope #ESTE ES EL PARAMETRO K

def main():
    root = Tk()
    App(root) #aplicacion visual, normalmente definida como app
    root.mainloop() #para mantener en pantalla

if __name__ == '__main__':
    main()

