#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ejemplo de Generador de numeros aleatorios
#
# Ricardo Haro Calvo
# Feb 27, 2023
# ricardo.AT.haroware.DOT.com
#

import sys
import numpy as np

def game(value):
    rng = np.random.randint(1,3)
    if value == 1 and rng == 2:
        print("You lose Paper beats Rock")
    elif value == 1 and rng == 3:
        print("You win Rock beats Scissors")
    elif value == 2 and rng == 1:
        print("You win Paper beats Rock")
    elif value == 2 and rng == 3:
        print("You lose Scissors beat Paper")
    elif value == 3 and rng == 1:
        print("You lose Rock beats Scissors")
    elif value == 3 and rng == 2:
        print("You win Scissors beat Paper")
    else:
        print ("Tie!")
    play_again = input("Play again? (y/n)")
    if play_again.lower() != "y":
        sys.exit()
    else:
        main()


def play(select):
    if (select) not in (1,2,3,4):
        print("Not a valid number")
        sys.exit(2)
    elif select == 4:
        sys.exit(2)
    else:
        game(select)

def main():
    print("Lets play Rock Paper, Scissors!")
    print("")
    print("Select a move")
    print("1.- Rock")
    print("2.- Paper")
    print("3.- Scissors")
    print("4.- Exit")
    while True:
        try:
            option = int(input("Select 1-4:"))
            break
        except ValueError:
            print("Please select a valid option")
    play(option)

if __name__ == '__main__':
    main()

