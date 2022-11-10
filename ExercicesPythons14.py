# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:13:38 2022

@author: st4r4x
"""
# Exercice 14:


def initialisationJeu(mot):
    mot_masque = []
    for i in range(len(mot)):
        if i == 0:
            mot_masque.append(mot[i])
        else:
            mot_masque.append("_")
    return mot_masque


def verification(lettre, mot):
    isIn = False
    for i in mot:
        if lettre == i:
            isIn = True
    return isIn


def affichageMot(lettre, mot, mot_affiche_precedent):
    mot_affiche = mot_affiche_precedent
    mot_stocke = list(mot)
    if verification(lettre, mot) is True:
        for i in range(len(mot_stocke)):
            if mot_stocke[i] == lettre:
                mot_affiche[i] = mot_stocke[i]
    return mot_affiche


def jeu(mot):
    mot_affiche = initialisationJeu(mot)
    print(mot_affiche)
    mot_stocke = list(mot)
    gagne = False
    cpt = 0
    while not gagne:
        if cpt <= 4:
            lettre = input("Entrez la lettre : ")
            if verification(lettre, mot_stocke) is True:
                mot_affiche = affichageMot(lettre, mot_stocke, mot_affiche)
                print(mot_affiche)
                if mot_affiche == mot_stocke:
                    gagne = True
                    print("Vous avez gagné")
            else:
                cpt += 1
                if 5-cpt > 1:
                    print(f"Plus que {5-cpt} vies")
                elif 5-cpt == 1:
                    print("C'est votre dernière vie")
        else:
            print("Vous avez perdu")
            return


jeu("anticonstitutionellement")
