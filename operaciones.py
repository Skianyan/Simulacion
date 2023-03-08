#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Codigos que se repiten en las clases
#
import datetime

class Aleatorios:
    def __init__(self, inicio, fin, cantidad):
        # Inicio de Intervalo
        self.inicio = inicio
        # Fin de intervalo
        self.fin = fin
        # Cantidad de numeros aleatorios por generar
        self.cantidad = cantidad
        # Valor del parametro t del generador
        self.parametro_t = 1649
        # Valor del parametro bandera del generador
        self.bandera = 1
        # Valor del modulo para el generador
        self.modulo = 2 ** 31

    def generador(self):
        a= (8 * self.parametro_t) + (self.bandera * 3)
        x = [datetime.now().microsecond]
        for i in range(1, self.cantidad + 1):
            valor = (a * x[i - 1]) % self.modulo
            x.append(valor)
        x.pop(0)
        aleatorios = [aleatorio / self.modulo for aleatorio in x]
        return aleatorios

    def intervalo(self):
        pendiente = (self.fin - self.inicio)
        valores_intervalos = [self.inicio + pendiente * j for j in self.generador()]
        return valores_intervalos

class withNumpy:
    def __init__(self, inicio, fin, costo_a, costo_b, costo_c, cantidad):
        # Inicio de Intervalo
        self.inicio = inicio
        # Fin de intervalo
        self.fin = fin
        # Costos de distribucion tirangular
        self.costo_a = costo_a
        self.costo_b = costo_b
        self.costo_c = costo_c
        # Cantidad de numeros aleatorios por generar
        self.cantidad = cantidad
        # Valor del parametro t del generador
        self.parametro_t = 1649
        # Valor del parametro bandera del generador
        self.bandera = 1
        # Valor del modulo para el generador
        self.modulo = 2 ** 31


class Contra:
    def __init__(self,parametro_a, modulo, semilla, cantidad):
        # Valores para utilizar el generador de aleatorios
        self.parametro.a = parametro_a
        self.modulo = modulo
        # Semilla para crear los aleatorios
        self.semilla = semilla
        # Número de aleatorios que se van a ocupar
        self.cantidad = cantidad

    def generar(self):
        #Se crean al arreglo que genera los valores aleatorios
        aleatorios = [self.semilla]
        for i in range(self.cantidad + 1):
            temp = (self.parametro_a * aleatorios[i-1]) % self.modulo
            aleatorios.append(temp)
        aleatorios.pop(0)
        aleatorios = [valor / self.modulo for valor in aleatorios]
        return aleatorios