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
from _datetime import datetime

class Aleatorios(object):
    def __init__(self, parametro_t, bandera, modulo, cantidad, decimales, **kwargs):
        self.parametro_t = parametro_t
        self.bandera = bandera
        self.modulo = modulo
        self.cantidad = cantidad
        self.decimales = decimales
        for key, value in kwargs.items():
            if key in ('-a', 'inicio'):
                if int(value) <= 0:
                    print("El inicio debe ser un numero positivo")
                    sys.exit(2)
                self.inicio = int(value)
            elif key in ('-b', 'fin'):
                if int(value) <= 0:
                    print("El fin debe ser un numero positivo")
                    sys.exit(2)
                self.fin = int(value)
            elif key in ('-t', 'parametro_t'):
                if int(value) <= 0:
                    print("El parametro t debe ser un numero positivo")
                    sys.exit(2)
                self.parametro_t = int(value)
            elif key in ('-f', '--flag'):
                self.bandera = int(value)
            elif key in ('-n', '--cantidad'):
                if int(value) <= 0:
                    print("La cantidad debe ser un numero positivo")
                    sys.exit(2)
                self.cantidad = int(value)
            elif key in ('-d', '--decimales'):
                if int(value) <= 0:
                    print("No es posible redondear una cantidad negativa")
                    sys.exit(2)
                self.decimales = int(value)

class Generar(Aleatorios):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def archivo(self, valores):
        data = []
        header = ['num', 'valor']
        for i in range(len(valores)):
            data.append([i+1, valores[i]])
        with open("salida.csv", "m", encoding="UTF-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        print("El archivo ha sido creado")

    def simular(self):
        parametro_a = 8 * self.parametro_t + (self.bandera * 3)
        now = datetime.now()
        seed = now.microsecond
        x = [seed]
        for i in range(1, self.cantidad + 1):
            valor = (parametro_a * x[i - 1]) % self.modulo
            x.append(valor)
        x.pop(0)
        aleatorios = [aleatorio / self.modulo for aleatorio in x]
        pendiente = (self.fin_intervalo - self.inicio.intervalo)

        valores_intervalos = [round(self.fin_intervalo + pendiente * j, self.decimales) for j in aleatorios]
        self.archivo(valores_intervalos)

def main(**kwargs):
    # Valor del parametro t del generador
    parametro_t = 1649
    # Valor del parametro bandera del generador
    bandera = 1
    # Valor del modulo para el generador
    modulo = 2 ** 31
    # Valor del parametro n del generador
    cantidad = 4
    # Valor del parametro d del generador
    decimales = 2
    inicio = Generar(parametro_t,bandera,modulo,cantidad,decimales,**kwargs)

    aleatorios = inicio.simular()

    for aleatorio in aleatorios:
        print(aleatorio)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='simula',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
        Generador de números pseudoaleatorios empleando el método congruencial
                        x_(n+1) = (ax_n) mod (m)
        donde la construcción del arreglo x está en función a un dato inicial X0 llamado seed.
        Los valores a, b, m son enteros positivos, y el valor m debe ser superior a cualquiera de
        los datos anteriores.
        El algoritmo generará un arreglo de <n> datos, que es un parámetro que el usuario debe
        indicar, asi como la cantidad por decimales a emplear
        """,
        epilog="""
        En caso de no declarar valores, el sistema tendrá parámetros predefinidos.
        """
    )

parser.add_argument('-a', '--inicio',
                    help='Valor inicial',
                    nargs='1', type=int, required=True)
parser.add_argument('-b', '--fin',
                    help='Valor final',
                    nargs='1', type=int, required=True)
parser.add_argument('-t', '--termino_t', default=1649,
                    help='Coeficiente t del generador',
                    nargs='?', type=int, required=False)
parser.add_argument('-f', '--flag', default=1,
                    help='Determina si se emplea suma o resta (default 1)',
                    nargs='?', type=int, choices=[1,-1], required=False)
parser.add_argument('-n', '--termino_n', default=4,
                    help='Numeros aleatorios por generar (default 4)',
                    nargs='?', type=int, required=False)
parser.add_argument('-d', '--termino_d', default=2,
                    help='Redondeo de decimales (default 2)',
                    nargs='?', type=int, required=False)
parser.parse_args()

main(**dict(arg.split('=') for arg in sys.argv[1:]))