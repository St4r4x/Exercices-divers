# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:30:15 2022

@author: st4r4x
"""
# Exercice 8 : Le bibliothécaire


import random
import string
alphabet = list(string.ascii_lowercase)
listeA = []

# Création de la liste de lettre aléatoire
for i in range(100):
    listeA.append(alphabet[random.randint(0, 25)])


def comptageLettreSimple(lettre):
    comptage = 0
    for i in listeA:
        if i == lettre:
            comptage += 1
    return comptage


def comptageLettre():
    comptageTotal = []
    for j in alphabet:
        comptage = 0
        for i in listeA:
            if i == j:
                comptage += 1
        comptageTotal.append(comptage)
        comptageTotal.append(j)
    return comptageTotal


print(comptageLettre())
