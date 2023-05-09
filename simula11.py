#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simulador de cálculo de probabilidad
# basandose en la media
#
# Ricardo Haro Calvo
# Abril 24, 2023
# ricardo.AT.haroware.DOT.com
#

import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("280x560")
        self.title("Calculo de utilidad")
        # Se inicializa la informacion
        self.precio = tk.DoubleVar() # Informacion del precio
        self.venta_minima = tk.IntVar() # Minima cantidad de unidades a vender
        self.venta_maxima = tk.IntVar() # Maxima cantidad de unidades a vender
        self.costo_fijo = tk.DoubleVar() # Costo fijo
        self.costo_pesimista = tk.DoubleVar() # Costo pesimista
        self.costo_probable = tk.DoubleVar() # Costo probable
        self.costo_optimista = tk.DoubleVar() # Costo optimista
        self.simulacion = tk.StringVar() # Tipo de simulacion a realizar
        self.repeticiones = tk.IntVar() # Duracion en años o meses que se realiza
        # Se crean los campos
        self.crear_widgets()

    def crear_widgets(self):
        datos = Frame(self)
        datos.pack(fill=tk.X)
        ttk.Label(datos,text="Precio del producto", justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        precio = Entry(datos, textvariable=self.precio)
        precio.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Venta Minima estimada", justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        venta_minima = Entry(datos, textvariable=self.venta_minima)
        venta_minima.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Venta Maxima estimada", justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        venta_maxima = Entry(datos, textvariable=self.venta_maxima)
        venta_maxima.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Costo Fijo", justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        costo_fijo = Entry(datos, textvariable=self.costo_fijo)
        costo_fijo.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Costo pesimista (a)", justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        costo_pesimista = Entry(datos, textvariable=self.costo_pesimista)
        costo_pesimista.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Costo probable (b)", justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        costo_probable = Entry(datos, textvariable=self.costo_probable)
        costo_probable.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Costo optimista (c)", justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        costo_optimista = Entry(datos, textvariable=self.costo_optimista)
        costo_optimista.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Señale el tipo de simulacion a realizar",
                  justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        forma = ttk.Combobox(datos, textvariable=self.simulacion, state='readonly',
                             values=['Por años', 'Por meses'])
        forma.pack(anchor=tk.W,padx=10,pady=5,fill=tk.X)
        forma.current()

        ttk.Label(datos, text="Periodo de la simulacion", justify=LEFT).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        repeticiones = Entry(datos, textvariable=self.repeticiones)
        repeticiones.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        tk.Button(datos,text="Simular", command=lambda: self.simula()).pack(side=tk.LEFT,padx=10,pady=5)
        tk.Button(datos,text="Salir", command=lambda: self.quit()).pack(side=tk.LEFT,padx=10,pady=5)

    def valida(self):
        bandera = 0
        if not self.precio.get():
            messagebox.showerror("Error de Precio", "Se debe declarar el precio")
        else:
            bandera += 1
        if self.precio.get()<=0:
            messagebox.showerror("Valor incongruente", "El precio debe ser un valor positivo")
        else:
            bandera += 1
        if not self.venta_minima.get():
            messagebox.showerror("Error de Venta Minima", "Se debe declarar la Venta Minima")
        else:
            bandera += 1
        if self.venta_minima.get()<=0:
            messagebox.showerror("Valor incongruente", "La venta minima debe ser un valor positivo")
        else:
            bandera += 1

        if not self.venta_maxima.get():
            messagebox.showerror("Error de Venta Maxima", "Se debe declarar la Venta Maxima")
        else:
            bandera += 1
        if self.venta_maxima.get()<=0:
            messagebox.showerror("Valor incongruente", "La venta maxima debe ser un valor positivo")
        else:
            bandera += 1

        if not self.costo_fijo.get():
            messagebox.showerror("Error de Costo Fijo", "Se debe declarar el Costo Fijo")
        else:
            bandera += 1
        if self.costo_fijo.get()<=0:
            messagebox.showerror("Valor incongruente", "El costo fijo debe ser un valor positivo")
        else:
            bandera += 1

        if not self.costo_probable.get():
            messagebox.showerror("Error de Costo Probable", "Se debe declarar el Costo Probable")
        else:
            bandera += 1
        if self.costo_probable.get()<=0:
            messagebox.showerror("Valor incongruente", "El costo probable debe ser un valor positivo")
        else:
            bandera += 1

        if not self.costo_optimista.get():
            messagebox.showerror("Error de Costo Optimista", "Se debe declarar el Costo Optimista")
        else:
            bandera += 1
        if self.costo_optimista.get()<=0:
            messagebox.showerror("Valor incongruente", "El costo optimista debe ser un valor positivo")
        else:
            bandera += 1

        if not self.costo_pesimista.get():
            messagebox.showerror("Error de Costo Pesimista", "Se debe declarar el Costo Pesimista")
        else:
            bandera += 1
        if self.costo_pesimista.get()<=0:
            messagebox.showerror("Valor incongruente", "El costo pesimista debe ser un valor positivo")
        else:
            bandera += 1

        if not self.repeticiones.get():
            messagebox.showerror("Error de repeticiones", "Se deben declarar las repeticiones")
        else:
            bandera += 1
        if self.repeticiones.get()<=0:
            messagebox.showerror("Valor incongruente", "Las repeticiones deben ser valores positivo")
        else:
            bandera += 1

        tipo_calculo = self.lectura(self.simulacion.get())
        #if tipo_calculo == 1:
        #if tipo_calculo == 2:
        return bandera

    @staticmethod
    def lectura(combo):
        switch = {
            'Por años': 1,
            'Por meses': 2,
        }
        return switch.get(combo, 'e')

    def simula(self):
        if self.valida() == 16: #change to 18
            self.continuar()

    def continuar(self):
        tipo_simulacion = self.lectura(self.simulacion.get())
        if tipo_simulacion == 1:
            ventas_estimadas = np.random.randint(self.venta_minima.get(),
                                                 self.venta_maxima.get(),
                                                 (self.repeticiones.get(),
                                                   12,
                                                   30))
            costos_estimados = np.random.triangular(self.costo_pesimista.get(),
                                                    self.costo_probable.get(),
                                                    self.costo_optimista.get(),
                                                    (self.repeticiones.get(),
                                                     12,
                                                     30))
        else:
            ventas_estimadas = np.random.randint(self.venta_minima.get(),
                                                 self.venta_maxima.get(),
                                                 (self.repeticiones.get(),
                                                  4,
                                                  5))
            costos_estimados = np.random.triangular(self.costo_pesimista.get(),
                                                    self.costo_probable.get(),
                                                    self.costo_optimista.get(),
                                                    (self.repeticiones.get(),
                                                     4,
                                                     5))
            # Calculo del ingreso
            ventas_promedio = np.average(ventas_estimadas, 2)
            ingresos_promedios = ventas_promedio * self.precio.get()
            ingresos = []
            for i in ingresos_promedios:
                for j in i:
                    ingresos.append(j)
            # Calculo del costo
            costos_parciales = np.around(costos_estimados * ventas_estimadas, 2)
            costos_promedios = self.costo_fijo.get() + np.average(costos_parciales, 2)
            costos = []
            for i in costos_promedios:
                for j in i:
                    costos.append(j)
            # Calculo de la utilidad
            utilidad_promedio = np.subtract(ingresos_promedios, costos_promedios)
            utilidad = []
            for i in utilidad_promedio:
                for j in i:
                    utilidad.append(j)
            figure = plt.Figure(figsize=(6, 5), dpi=100)
            line = FigureCanvasTkAgg(figure, self)
            line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            plt.plot(ingresos, color='r', marker='o', label='Ingreso')
            plt.plot(utilidad, color='b', marker='+', label='Costo')
            plt.plot(utilidad, color='g', marker='x', label='Utilidad')
            plt.legend()
            plt.show()

if __name__ == '__main__':
    app = App()
    app.mainloop()