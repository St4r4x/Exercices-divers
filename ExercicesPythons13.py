# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 17:53:43 2022

@author: st4r4x

"""

# Exercice 13:
    
# le nain 1 fait 1 lingot
# le nain 2 fait 2 lingots
# le nain 3 fait 4 lingots
# le nain 4 fait 8 lingots
# le nain 5 fait 16 lingots
# le nain 6 fait 32 lingots
# le nain 7 fait 64 lingots
nain1 = 1
nain2 = 2
nain3 = 4
nain4 = 8
nain5 = 16
nain6 = 32
nain7 = 64
poids_theorique = 127000
liste_nain = [nain7, nain6, nain5, nain4, nain3, nain2, nain1]
nom_nain = ["Atchoum", "Simplet", "Dormeur", "Prof", "Grincheux", "Joyeux", "Timide"]


def poidsOrVole(poids_pesee):
    if poids_pesee < 126873:
        print("Erreur de pesée")
        return False
    or_vole = poids_pesee - poids_theorique
    or_vole = -or_vole
    return or_vole


def nainCoupable(or_vole):
    liste_coupable = []
    cpt = 0
    for i in liste_nain:
        if or_vole//i == 1:
            liste_coupable.append(nom_nain[cpt])
            or_vole = or_vole % i
        cpt += 1
    return liste_coupable


print(nainCoupable(poidsOrVole(int(input("Entrez le poids en grammes de la pesée des 127 lingots : ")))))
