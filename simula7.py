#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ejemplo de Generador de numeros aleatorios
#
# Ricardo Haro Calvo
# Feb 14, 2023
# ricardo.AT.haroware.DOT.com
#

import sys
import numpy as np

def generate_pass(num_char):
    upper = ['A','B','C','D','F','G','J','K','L','O','Q','R','N','V','W','Z','Y']
    lower = ['a','b','c','d','e','g','h','i','k','n','p','s']
    numbers = ['0','2','3','5','7','8','9']
    symbols = ['#','!','$','&','*','+']
    concatpass = ''
    for i in range(num_char):
        option = np.random.randint(1,4)
        np.random.shuffle(upper)
        np.random.shuffle(lower)
        np.random.shuffle(numbers)
        np.random.shuffle(symbols)
        if option == 1:
            value = upper[np.random.randint(0, len(upper)-1)]
            concatpass = concatpass + value
        elif option == 2:
            value = lower[np.random.randint(0, len(lower) - 1)]
            concatpass = concatpass + value
        elif option == 3:
            value = numbers[np.random.randint(0, len(numbers) - 1)]
            concatpass = concatpass + value
        else:
            value = symbols[np.random.randint(0, len(symbols) - 1)]
            concatpass = concatpass + value
    return concatpass

def validation(num_char):
    if num_char <= 0:
        print("Invalid number of characters")
        sys.exit(2)
    else:
        passcode = generate_pass(num_char)
        print(passcode)


def main():
    while True:
        try:
            n = int(input("Number of characters for password: "))
            break
        except ValueError:
            print("Please insert a valid number of characters")
    validation(n)

if __name__ == '__main__':
    main()
