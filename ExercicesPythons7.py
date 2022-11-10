# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:10:41 2022

@author: st4r4x
"""

# Exercice 7 : Upside Down
import random
listeExo = (list(range(10)))
listeRandom = []
for i in range(100):
    aleatoire = random.randint(0, 100)
    listeRandom.append(aleatoire)


def reverseListe(liste):
    listetemp = []
    for i in range(len(liste)-1):
        listetemp.append(liste[-i-1])
    return listetemp


def funReverse(liste):
    liste1 = liste[:]
    liste2 = []
    for i in range(10):
        a = liste1[-1]
        liste.pop()
        liste2.append(a)
    return liste2


def funReverseValues(liste):
    liste_temp = []
    for i in range(len(liste)-1, -1, -1):
        print(i)
        liste_temp.append(liste[i])
    return liste_temp


def funReverseValuesAnto(liste):
    list2 = liste[::-1]
    return list2
