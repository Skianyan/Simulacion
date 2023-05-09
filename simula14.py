#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Problema de paracaidista
# Utilizando el metodo de Runge-Kutta
#
# Ricardo Haro Calvo
# Mayo 4, 2023
# ricardo.AT.haroware.DOT.com
#
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
class App():
    def __init__(self, root):
        self.root = root
        root.title("Paracaidista") #Titulo
        root.geometry("450x300") #dimensiones
        #Inicializa la informacion
        self.VelocidadAvion = tk.IntVar() #Pedir la velocidad del avion
        self.VelocidadViento = tk.IntVar() #Requerir la velocidad del viento
        #Crear los campos
        self.crear_widgets()

    def crear_widgets(self):
        #Se crea el frame para requerir informacion
        datos = Frame(self.root, height=2, bd=1, relief=SUNKEN) #widget properties
        datos.pack(fill=X, padx=10, pady=5)                #
        #Captura de velocidad del avion
        ttk.Label(datos, text="Velocidad del avion", justify=LEFT).pack(fill=BOTH, expand=TRUE)
        velocidad_avion = Entry(datos, textvariable=self.VelocidadAvion, width=16)
        velocidad_avion.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(datos, text="Velocidad del viento", justify=LEFT).pack(fill=BOTH, expand=TRUE)
        velocidad_viento = Entry(datos, textvariable=self.VelocidadViento, width=16)
        velocidad_viento.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        # Se crea un frame para los botones
        botones = Frame(self.root, height=2, bd=1, relief=SUNKEN)
        botones.pack(fill=X, padx=10, pady=5)
        ttk.Button(botones, text="Graficar", command=lambda:self.simular()).pack(side=LEFT, padx=10, pady=5)
        ttk.Button(botones, text="Salir", command=lambda:self.root.quit()).pack(side=LEFT, padx=10, pady=5)

    def verificar(self):
        bandera = 0
        # Validacion de Velocidad Avion
        if not self.VelocidadAvion.get():
            messagebox.showerror("Error", "No se ha declarado la velocidad del avion")
        else:
            if self.VelocidadAvion.get() < 0:
                messagebox.showerror("Velocidad no validada", "No se puede declarar una velocidad negativa")
            else:
                bandera += 1

        #Validacion de Velocidad Viento
        if not self.VelocidadViento.get():
            messagebox.showerror("Error","No se ha declarado la velocidad del avion")
        else:
            if self.VelocidadViento.get() < 0:
                messagebox.showerror("Velocidad no validada", "No se puede declarar una velocidad negativa")
            else:
                bandera += 1
        return bandera
    @staticmethod
    def rk4(f, x0, y0, x1, n):
        vx = [0] * (n + 1)
        vy = [0] * (n + 1)
        h = (x1 - x0) / float(n)
        vx[0] = x = x0
        vy[0] = y = y0
        for i in range(1, n + 1):
            k1 = h * f(x, y)
            k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
            k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
            k4 = h * f(x + h, y + k3)
            vx[i] = x = x0 + i * h
            vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
        return vx, vy

    def funcion(self, x=None, y=None):
        velocidad_viento = self.VelocidadViento.get()
        A = 32/velocidad_viento
        B = math.sqrt(velocidad_viento)
        return A * (B - y) * (B + y)
    def simular(self):
        if self.verificar() == 2:
            self.resolver()

    def resolver(self):
        #Primero, se crea un figura contenedora
        fig = Figure(figsize=(5, 5))
        vx,vy = self.rk4(self.funcion, 0, self.VelocidadViento.get(), 2, 1000)
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
def main():
    root = Tk()
    App(root) #aplicacion visual, normalmente definida como app
    root.mainloop() #para mantener en pantalla

if __name__ == '__main__':
    main()

