#!/usr/bin/env python
# -*-coding: utf-8 -*-
#
# #####
# ####
#
# feb 14,2023
# #########
#

import sys
import argparse
from operaciones import Aleatorios
import csv

class verificar(object):
    def __init__(self,precio,archivo, cantidad, decimales, **kwargs):
        self.precio = precio
        self.archivo = archivo
        self.cantidad = cantidad
        self.decimales = decimales
        for key, value in kwargs.items():
            if key in ('-a', '--dminima'):
                if float(value)<= 0:
                    print("la demanda minima no puede ser negativa")
                    sys.exit(2)
                self.dminima = float(value)
            elif key in ('-b', '--dmaxima'):
                if float(value)<= 0:
                    print("la demanda maxima no puede ser negativa")
                    sys.exit(2)
                self.dmaxima = float(value)
            elif key in ('-p', '--precio'):
                if float(value)<= 0:
                    print("el precio debe de ser positivo")
                    sys.exit(2)
                self.precio = float(value)
            elif key in ('-t', '--parametro'):
                if int(value) <= 0:
                    print('el parametro t debe de ser entero positivo')
                    sys.exit(2)
                self.parametro_t = int(value)
            elif key in ('-B', '--bandera'):
                self.bandera = int(value)
            elif key in ('-n', '--cantidad'):
                if int(value) <= 0:
                    print('No es posible generar una cantidad negativa de aleatorios')
                    sys.exit(2)
                self.cantidad =int(value)
            elif key in ('-d', '--decimales'):
                if int(value) < 0:
                    print('no es posible redondear de forma negativa')
                    sys.exit(2)
                self.decimales = int(value)


class utilidad(verificar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)

    def crear_archivo(self, valores):
        data = []
        header = ['Num', 'Valor']
        for i in range(len(valores)):
            data.append([i+1, valores[i]])
        with open(self.archivo, "w", encoding='UTF-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(data)
        print('el archivo se ha generado')


    def simular(self):
        aleatorios = Aleatorios(self.dminima, self.dmaxima, self.cantidad)
        demanda = aleatorios.intervalo()
        ingreso =[round(self.precio * j, 2) for j in demanda]
        self.crear_archivo(ingreso)


def main(**kwargs):
    precio = 60 # precio
    archivo = "salida1.csv" #nombre de salida
    cantidad = 50 # cantidad de numeros aleatorios
    decimales = 2 # decimales a redondear 
    valores = utilidad(precio,archivo,cantidad,decimales,**kwargs)
    valores.simular()


if __name__ =='__main__':
    parser = argparse.ArgumentParser(
        prog='simula5',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    description="""
        Generador para el calculo de utilidades , empleando el metodo congruencial multiplicativo
        para ello , se requiere calcular primeramente el ingreso , determinado mediante 
                                   ingreeso= (precio venta)(demanda)
        donde la demanda es un valor aleatorio comprendiendo en el intervalo [a,B] que  son datos 
        ingresados por el usuario ,para posteriormente multiplicarlos por el precio (p) de venta.
          """,
        epilog="""
        El usuario podra determinar la cantidad de valores pseudo-aleatorios por ser generados 
        mediante la designacion del valor de la variable -n o su forma alterna --cuantos.
        Tambien  de la cantidad de decimales por emplear por medio de la variable -d o 
        --decimales la informacion es enviada a un archivo ,llamado salida.csv pero puede 
        ser modificado mediante el parametro -f.
        """
    )
    parser.add_argument('-a', '--dminima',
                        help=' minima demanda del producto (default: %(default)s )',
                        nargs=1, type=float, required=True)
    parser.add_argument('-b', '--dmaxima', default=5678,
                        help='maxima demanda del producto (default: %(default)s )',
                        nargs=1, type=float, required=True)
    parser.add_argument('-p', '--precio',default=60,
                        help='precio de venta por unidad (default: %(default)s )',
                        nargs='?', type=int, required=False)
    parser.add_argument('-n', '--cantidad', default=50,
                        help='numero de valores a generar  (default: %(default)s )',
                        nargs='?', type=int, required=False)
    parser.add_argument('-f', '--archivo', default="salida.csv",
                        help='nombre del archivo de salida (default: %(default)s )',
                        nargs='?', type=str, required=False)
    parser.parse_args()
    main(**dict(arg.split('=') for arg in sys.argv[1:]))