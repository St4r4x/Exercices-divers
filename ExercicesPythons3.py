# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:26:30 2022

@author: st4r4x
"""

# Exercice 3 : Parcours de liste

# Création de la liste

liste = (list(range(100)))

# Création de la fonction de parcours


def parcoursListe():
    for n in liste:
        print(f"Je suis l'élément {n} dans la liste")

# Création de la fonction de parcours spéciale


def parcoursListeSpe():
    i = 0
    boole = True
    while i < len(liste)-1:
        if boole:
            i = i+3
            print(f"Je suis l'élément {liste[i]} dans la liste")
            boole = not boole
        else:
            i = i-1
            print(f"Je suis l'élément {liste[i]} dans la liste")
            boole = not boole


# Création de la fonction de parcours avec création de liste

def parcoursListeCrea(liste):
    liste_paire = []
    liste_impaire = []
    for n in liste:
        if n % 2 == 0:
            liste_paire.append(n)
        else:
            liste_impaire.append(n)
    return liste_paire, liste_impaire


liste_paire1, liste_impaire2 = parcoursListeCrea(liste)
