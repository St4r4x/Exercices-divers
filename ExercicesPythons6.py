# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:57:59 2022

@author: st4r4x
"""
import random

# Création liste avec des nombre aléatoire


def listeAleatoire():
    liste = []
    for i in range(100):
        aleatoire = random.randint(0, 100)
        liste.append(aleatoire)
    return liste


listeA = listeAleatoire()

# Recherche de la valeur maximum de la liste


def maxListe(listeA):
    maxi = 0
    positionmaxi = 0
    i = 0
    while i < len(listeA):
        if maxi < listeA[i]:
            maxi = listeA[i]
            positionmaxi = i
        i += 1
    return maxi, positionmaxi


maxi = maxListe(listeA)
print(f"La valeur maxi est {maxi[0]} et sa position est {maxi[1]}")

# Recherche de la valeur min de la liste


def minListe(listeA):
    mini = 100
    positionmini = 0
    i = 0
    while i < len(listeA):
        if mini > listeA[i]:
            mini = listeA[i]
            positionmini = i
        i += 1
    return mini, positionmini


mini = minListe(listeA)
print(f"La valeur mini est {mini[0]} et sa position est {mini[1]}")
