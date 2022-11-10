# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:40:46 2022

@author: st4r4x
"""
# Exercice 9 : Le loto

import random
liste = list(range(1, 50))


def loto():
    tirage = []
    numero = 0
    for i in range(5):
        numero = liste[random.randint(0, len(liste)-1)]
        liste.remove(numero)
        tirage.append(numero)
    return tirage


print(loto())
