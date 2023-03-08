#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Clase para encriptar una contraseña
#
# Ricardo Haro Calvo
# Feb 14, 2023
# ricardo.AT.haroware.DOT.com
#
import argparse
import sys
import math
from operaciones import Contra
import numpy as np

class Parametros(object):
    def __init__(self, parametro_a, modulo, **kwargs):
        self.parametro_a = parametro_a
        self.modulo = modulo
        for key, value in kwargs.items():
            if key in ("-p","-parametro_a"):
                self.contrasenia = value
                semilla = 0
                for caracter in value:
                    if caracter in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
                        semilla += ord(caracter)
                    self.semilla = semilla
            elif key in ("-a","--generador"):
                if int(value) <= 0:
                    print("No se puede emplear un parámetro negativo")
                    sys.exit(2)
                self.parametro_a = int(value)
            elif key in ("-m", "--modulo"):
                if int(value) <= 0:
                    print("No se puede utilizar el modulo con un valor negativo")
                    sys.exit(2)
                self.modulo = int(value)
            elif key in ("-s", "--semilla"):
                if int(value) <= 0:
                    print("No se puede emplear como semilla un valor negativo")
                    sys.exit(2)
                self.semilla = int(value)
        if self.parametro_a >= self.modulo or self.semilla >= self.modulo:
            print("El valor del modulo debe ser superior tanto al parametro como a la semilla")
            print("No es posible continuar")
            sys.exit(2)
class Encriptar(Parametros):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    @staticmethod
    def cambiardigitos(digitos):
        decimales = [10, 11, 12, 13, 14, 15]
        hexadecimal = ['A', 'B', 'C', 'D', 'E', 'F']
        for c in range(7):
            if digitos == decimales[c-1]:
                digitos = hexadecimal[c-1]
        return digitos
    def decimalhexadecimal(self, decimal):
        hexadecimal = ''
        while decimal != 0:
            rem = self.cambiardigitos(decimal % 16)
            hexadecimal = str(rem) + hexadecimal
            decimal = int(decimal / 16)
        return hexadecimal
    def encriptar(self):
        #se crea lo que será la nueva contraseña
        palabra = ''
        inicio = Contra(self.parametro_a, self.modulo, self.semilla, len(self.contrasenia))
        valores_aleatorios = inicio.generar()
        #se multiplica los valores aleatorio por los valores ASCII de cada letra
        for i in range(len(self.contrasenia)):
            caracter = self.contrasenia(i)
            asci = ord(caracter)
            termino = self.decimalhexadecimal(math.floor(asci * valores_aleatorios[i]))
            palabra += termino
        return palabra
def main(**kwargs):
    # Valor de parámetro a
    parametro_a = 269
    # Valor de modulo m
    modulo = 2 ** 31

    iniciar = Encriptar(parametro_a, modulo, **kwargs)
    #
    nueva_contrasenia = iniciar.encriptar()
    print(nueva_contrasenia)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='simula8',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
        Programa dedicado a encriptar contraseñas
        Se emplea el generador de numeros aleatorios en forma congruencial, donde la semilla se obtiene
        al sumar el valor ASCII de cada vocal. Posteriormente, se multiplica por cada letra de la palabra 
        a encriptar por su correspondiente aleatorio, para que por último se convierta a una cadena
        hexadecimal.
        """,
        epilog="""
        El sistema obtiene e manera automática la semilla, salvo que sea el usuario quien declare otro valor.
        Se muestra en pantalla el termino encriptado correspondiente.
        """
    )
parser.add_argument('-p','--palabra', help="Contraseña a ser encriptada", nargs=1, required=True)
parser.add_argument('-a','--generador', default=269,
                    help="Multiplicador del generador congruencial aleatorio (default: %(defaults)s)",
                    nargs='?', type=int, required=False)
parser.add_argument('-m','--modulo', default=2**31,
                    help="Modulo del generador congruencial aleatorio (default: %(defaults)s)",
                    nargs='?', type=int, required=False)
parser.add_argument('-s','--semilla',
                    help="Semilla a ser empleada para el algoritmo",
                    nargs='?', type=int, required=False)
parser.parse_args()
main(**dict(arg.split('=') for arg in sys.argv[1:]))

