#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ejemplo de Generador de numeros aleatorios
#
# Ricardo Haro Calvo
# Feb 14, 2023
# ricardo.AT.haroware.DOT.com
#
import csv
import sys
import argparse
from operaciones import Aleatorios


class Verificar(object):
    def __init__(self, precio, archivo, cantidad, **kwargs):
        self.precio = precio
        self.archivo = archivo
        self.cantidad = cantidad
        for key, value in kwargs.items():
            if key in ('-a', 'dminima'):
                if float(value) <= 0:
                    print("La demanda minima no puede ser negativa")
                    sys.exit(2)
                self.dminima = float(value)
            elif key in ('-b', 'dmaxima'):
                if float(value) <= 0:
                    print("La demanda maxima no puede ser negativa")
                    sys.exit(2)
                self.dmaxima = float(value)
            elif key in ('-p', 'precio'):
                if float(value) <= 0:
                    print("El precio debe ser un numero positivo")
                    sys.exit(2)
                self.parametro_t = float(value)
            elif key in ('-n', '--cantidad'):
                if int(value) <= 0:
                    print("La cantidad debe ser un numero positivo")
                    sys.exit(2)
                self.cantidad = int(value)
            elif key in ('-f', '--archivo'):
                self.decimales = int(value)

class Utilidad(Verificar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def crear_archivo(self, valores):
        data = []
        header = ['num', 'valor']
        for i in range(len(valores)):
            data.append([i + 1, valores[i]])
        with open(self.archivo, "m", encoding="UTF-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        print("El archivo ha sido creado")

    def simular(self):
        aleatorios = Aleatorios(self.dminima, self.dmaxima, self.cantidad)
        demanda = aleatorios.intervalo()
        ingreso = [round(self.precio * j,2) for j in demanda]
        self.crear_archivo(ingreso)


def main(**kwargs):
    # Precio de venta
    precio = 60
    # Nombre archivo de salida
    archivo = "salida.csv"
    # Valor del parametro n del generador
    cantidad = 50
    # Valor del parametro d del generador
    decimales = 2
    valores = Utilidad(precio, archivo, cantidad, decimales, **kwargs)
    valores.simular()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='simula5',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
        Generador para el calculo de utilidades, empleando el metodo congruencial multiplicativo.
        Para ello se requiere calcular primero el ingreso, determinado mediante.
                                Ingreso = (Precio Venta)(Demanda)
        donde la demanda es un valor aleatorio comprendido en el intervalo [a,b], que son datos
        ingresados por el usuario, para posteriormente multiplicarlos por el precio (p) de venta.
        """,
        epilog="""
        El usuario podra determinar la cantidad de valores pseudo-aleatorios por ser generados, mediante
        la designacion del valor de la variable -n o su forma alterna --cuantos.
        Tambien, de la cantidad de decimales por emplear por medio de la variable -d o -decimales.
        La informacion es enviada a un archivo, llamado "salida.csv" pero que puede ser modificado mediante
        el parametro -f.
        """
    )

parser.add_argument('-d', '--dminima',
                    help='Demanda minima del producto',
                    nargs=1, type=float, required=True)
parser.add_argument('-D', '--dmaxima',
                    help='Demanda maxima del producto',
                    nargs=1, type=float, required=True)
parser.add_argument('-p', '--precio', default=60,
                    help='Precio de venta por unidad (default: %(default)s)',
                    nargs='?', type=float, required=False)
parser.add_argument('-n', '--cantidad', default=50,
                    help='Cantidad de valores por generar (default: %(default)s)',
                    nargs='?', type=int, required=False)
parser.add_argument('-f', '--archivo', default="salida.csv",
                    help='Nombre del archivo de salida (default: %(default)s)',
                    nargs='?', type=str, required=False)
parser.parse_args()

main(**dict(arg.split('=') for arg in sys.argv[1:]))