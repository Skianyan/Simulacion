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