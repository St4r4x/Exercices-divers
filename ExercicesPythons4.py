# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:26:57 2022

@author: st4r4x
"""

# Exercice 4 : Plus fort que la pomme

# Création de la liste
liste = (list(range(1000)))
n = len(liste)-1

# Création de la fonction d'addition des l'élément


def additionListe(liste):
    somme = 0
    for n in liste:
        somme = n+somme
    return somme


# autre méthode
def funcSum(liste):
    som = sum(liste)
    print(som)


def funGauss(n):
    return n*(n+1)/2


print(additionListe(liste))
print(funGauss(n))
