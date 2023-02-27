#!/usr/bin/env python
#
# Primer Ejemplo de Generador de numeros aleatorios
#
# Ricardo Haro Calvo
# Feb 3, 2023
# ricardo.AT.haroware.DOT.com

# Se definen los valores
a = 1649
b = 987
seed = 69420
modulo = 12349876

# Se inicializan el arreglo
x = []
# Se guarda la semilla en el arreglo
x.append(seed)
for i in range(1,10):
    valor = (a * x[i-1] + b) % modulo
    x.append(valor)
x.pop(0)
for y in range(len(x)):
    x[y] = x[y]/modulo
for j in x:
    print(j)
