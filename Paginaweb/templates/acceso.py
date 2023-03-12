#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import math
class Contra:
    def __init__(self, login, contrasenia):
        # Valores para el generador congruencial
        self.parametro_a = 269
        self.modulo = 2 ** 31
        # Identificacion del usuario login
        self.login = login
        # Identificacion del usuario
        self.password = contrasenia

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
    def semilla(self):
        datos_acceso = self.login.split('0')
        usuario = datos_acceso[0]
        suma = 0
        for caracter in usuario:
            if caracter not in ('a','e','i','o','u'):
                suma += ord (caracter)
        return suma

    def generar(self):
        aleatorio=[self.semilla()]
        for i in range(len(self.password)+ 1):
            temp = (self.parametro_a * aleatorio[i-1]) % self.modulo
            aleatorio.append(temp)
        aleatorio.pop(0)
        aleatorios = [valor / self.modulo for valor in aleatorio]
        return aleatorios
    def encriptar(self):
        # Donde estará la contrasenia
        palabra = ''
        valores_aleatorios = self.generar()
        contrasenia = self.password
        #se multiplica los valores aleatorio por los valores ASCII de cada letra
        for i in range(len(self.contrasenia)):
            caracter_en_ascii = self.contrasenia(i)
            termino = self.decimalhexadecimal(math.floor(caracter_en_ascii * valores_aleatorios[i]))
            palabra += termino
        return palabra