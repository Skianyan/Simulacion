#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Runge-Kutta Method
#
# Ricardo Haro Calvo
# Mayo 3, 2023
# ricardo.AT.haroware.DOT.com
#
from math import sqrt
import matplotlib.pyplot as plt
def rk4(f, x0, y0, x1, n):
    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    h = (x1 - x0) / float(n)
    vx[0] = x = x0
    vy[0] = y = y0
    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        vx[i] = x = x0 + i * h
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return vx, vy

def f(x, y):
    return 5 * x**2 - 8 * x

if __name__ == '__main__':
    vx, vy = rk4(f, 2, 3, 10, 100)
    plt.plot(vx,vy)
    plt.show()

