#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Codigos que se repiten en las clases
#
import datetime
from numpy import random

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

    def generador(self):
        x = random.rand()


    def intervalo(self):
        pendiente = (self.fin - self.inicio)
        valores_intervalos = [self.inicio + pendiente * j for j in self.generador()]
        return valores_intervalos

