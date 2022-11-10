# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:05:59 2022

@author: st4r4x
"""
# Exercice 11: Chiffrement de Cesar

import string
alphabet = list(" "+string.ascii_lowercase)


def chiffrementCesar(phrase, clef):
    phrase_chiffre = []
    for i in phrase:
        cpt = 0
        for j in alphabet:
            if i == j:
                lettre_chiffre = alphabet[(cpt+clef) % len(alphabet)]
                phrase_chiffre.append(lettre_chiffre)
            cpt += 1
    return phrase_chiffre


def dechiffrementCesar(phrase, clef):
    phrase_dechiffre = []
    for i in phrase:
        cpt = 0
        for j in alphabet:
            if i == j:
                lettre_dechiffre = alphabet[(cpt-clef) % len(alphabet)]
                phrase_dechiffre.append(lettre_dechiffre)
            cpt += 1
    return phrase_dechiffre


def trouverIndiceLettre(lettre):
    cpt = 0
    for i in alphabet:
        if i == lettre:
            return cpt
        cpt += 1
    print("Cette lettre n'est pas dans l'alphabet")


def chiffrementCesarProf(phrase, clef):
    phraseChiffre = []
    for i in phrase:
        indiceActuel = trouverIndiceLettre(i)
        indiceNouveau_temp = indiceActuel+clef
        indiceNouveau = indiceNouveau_temp % len(alphabet)
        lettreNouveau = alphabet[indiceNouveau]
        phraseChiffre.append(lettreNouveau)
    return phraseChiffre


print(chiffrementCesar("les chaussettes de larchiduchesse sont elles seches", 5))
