#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Primer Ejemplo de Generador de numeros aleatorios
#
# Ricardo Haro Calvo
# Feb 3, 2023
# ricardo.AT.haroware.DOT.com
#

import sys
import argparse

class Aleatorios(object):
    def __init__(self,parametro_a,parametro_b,semilla,modulo,cantidad,decimales,**kwargs):
        self.parametro_a = parametro_a
        self.parametro_b = parametro_b
        self.semilla = semilla
        self.modulo = modulo
        self.cantidad = cantidad
        self.decimales = decimales
        for key, value in kwargs.items():
            if key in ('-a','--termino_a'):
                if int(value) <=0:
                    print("El parametro a debe ser un numero positivo")
                    sys.exit(2)
                self.parametro_a = int(value)
            elif key in ('-b','--termino_b'):
                if int(value) <=0:
                    print("El parametro b debe ser un numero positivo")
                    sys.exit(2)
                self.parametro_b = int(value)
            elif key in ('-S','--semilla'):
                if int(value) <=0:
                    print("La semilla debe ser un numero positivo")
                    sys.exit(2)
                self.semilla = int(value)
            elif key in ('-m','--modulo'):
                if int(value) <=0:
                    print("El modulo debe ser un numero positivo")
                    sys.exit(2)
                self.modulo = int(value)
            elif key in ('-n','--cantidad'):
                if int(value) <=0:
                    print("No se puede generar una cantidad negativa de numeros")
                    sys.exit(2)
                self.semilla = int(value)
            elif key in ('-d','--decimales'):
                if int(value) <=0:
                    print("No se puede redondear una cantidad negativa de numeros")
                    sys.exit(2)
                self.semilla = int(value)
            if self.modulo <= self.parametro_a or self.modulo <= self.parametro_b or self.modulo <= self.semilla:
                print("El valor Modulo debe ser superior a los parametros.")
                sys.exit(2)


class Generar(Aleatorios):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


    def simulador(self):
        x = [self.semilla]
        for i in range (1,self.cantidad+1):
            valor = (self.parametro_a * x[i-1] + self.parametro_b) % self.modulo
            x.append(valor)
        x.pop(0)
        aleatorios = [aleatorio/self.modulo for aleatorio in x]

def main(**kwargs):
    # Valor del parametro a del generador
    parametro_a = 1649
    # Valor del parametro b del generador
    parametro_b = 987
    # Valor de la semilla
    semilla = 69420
    # Valor del modulo para el generador
    modulo = 12349876
    # Aleatorios por crear
    cantidad = 5
    # Decimales por redondear
    decimales = 2
    iniciar = Generar(parametro_a,parametro_b,semilla,modulo,cantidad,decimales,**kwargs)
    aleatorios = iniciar.simulador()
    for aleatorio in aleatorios:
        print(aleatorio)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='simula',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
        Generador de números pseudoaleatorios empleando el método congruencial
                        x_(n+1) = (ax_n + b) mod (m)
        donde la construcción del arreglo x está en función a un dato inicial X0 llamado semilla.
        Los valores a, b, m son enteros positivos, y el valor m debe ser superior a cualquiera de
        los datos anteriores.
        El algoritmo generará un arreglo de <n> datos, que es un parámetro que el usuario debe
        indicar, asi como la cantidad por decimales a emplear
        """,
        epilog="""
        En caso de no declarar valores, el sistema tendrá parámetros predefinidos.
        """
    )
    parser.add_argument('-a','--termino_a',default=1649,
                        help='Coeficiente a del generador (default=%(default)s )',
                        nargs='?', type=int, required=False)
    parser.add_argument('-b', '--termino_b', default=987,
                        help='Coeficiente b del generador (default=%(default)s )',
                        nargs='?', type=int, required=False)
    parser.add_argument('-S', '--seed', default=69420,
                        help='Semilla del generador (default=%(default)s )',
                        nargs='?', type=int, required=False)
    parser.add_argument('-m', '--modulo', default=12349876,
                        help='Numero de aleatorios por generar (default=%(default)s )',
                        nargs='?', type=int, required=False)
    parser.add_argument('-n', '--cantidad', default=2,
                        help='Redondeo de decimales (default=%(default)s )',
                        nargs='?', type=int, required=False)

    parser.parse_args()

    main(**dict(arg.split('=') for arg in sys.argv[1:]))