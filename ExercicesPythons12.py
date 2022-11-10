# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:25:52 2022

@author: st4r4x
"""

# Exercice 12:

import string
alphabet = list(" "+string.ascii_lowercase)

# on fait une fonction qui trouve les indices des lettres


def trouverIndiceLettre(lettre):
    cpt = 0
    for i in alphabet:
        if i == lettre:
            return cpt
        cpt += 1
    print("Cette lettre n'est pas dans l'alphabet")

# on transforme la phrase en une liste comprenant les indices des lettres de la phrase


def indicePhrase(phrase):
    indice_phrase = []
    for i in phrase:
        indiceActuel = trouverIndiceLettre(i)
        indice_phrase.append(indiceActuel)
    return indice_phrase

# pareil pour la clef


def indiceClef(clef):
    indice_clef = []
    for i in clef:
        indiceActuel = trouverIndiceLettre(i)
        indice_clef.append(indiceActuel)
    return indice_clef

# le chiffrement additionne pour chaque indice l'indice de clef correspondant


def chiffrementVigenere(indice_phrase, indice_clef):
    cpt = 0
    phrase_chiffre = []
    for i in range(len(indice_phrase)):
        indice_global = indice_phrase[i]+indice_clef[cpt % len(indice_clef)]
        lettreNouveau = alphabet[indice_global % len(alphabet)]
        phrase_chiffre.append(lettreNouveau)
        cpt += 1
    return "".join(phrase_chiffre)

# pareil mais en soustrayant


def dechiffrementVigenere(indice_phrase, indice_clef):
    cpt = 0
    phrase_dechiffre = []
    for i in range(len(indice_phrase)):
        indice_global = indice_phrase[i]-indice_clef[cpt % len(indice_clef)]
        lettreNouveau = alphabet[indice_global % len(alphabet)]
        phrase_dechiffre.append(lettreNouveau)
        cpt += 1
    return "".join(phrase_dechiffre)


# Module de démarrage pour l'utilisateur
rep = input("Tapez 1 si vous voulez chiffrer ou 2 si vous voulez déchiffrer : ")
if rep == "1":
    print(chiffrementVigenere(indicePhrase(input("Ecrivez la phrase à chiffrer(sans majuscules et sans caractères accentués) : ")),
          indiceClef(input("Ecrivez la clé de chiffrage (sans majuscules et sans caractères accentués): "))))
if rep == "2":
    print(dechiffrementVigenere(indicePhrase(input("Ecrivez la phrase à déchiffrer (sans majuscules et sans caractères accentués): ")),
          indiceClef(input("Ecrivez la clé de déchiffrage (sans majuscules et sans caractères accentués): "))))
