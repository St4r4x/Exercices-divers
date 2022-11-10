# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:08:59 2022

@author: st4r4x
"""

# Exercice 10 : Le palindrome

import string
alphabet = list(string.ascii_lowercase)


def palindromeMot(mot):
    i = 0
    while i != len(mot):
        if mot[i] != mot[-i-1]:
            return False
        else:
            i += 1
    return True


def palindromeMotAnthony(mot):
    is_palindrome = False
    if mot == mot[::-1]:
        print("C'est un palindrome")
    else:
        print("Ce n'est pas un palindrome")


def palindromeNicolas(mot):
    for i in range(int(len(mot)/2)):
        a = mot[-1-i]
        b = mot[i]
        print(f"{a} et {b}")
        if a != b:
            return False
    return True


def nettoyage(phrase):
    liste_vide = []
    for i in phrase:
        if i == " ":
            walou = 0
        if i == "," or i == "." or i == "?" or i == "!":
            walou = 0
        if i == "é":
            liste_vide.append("e")
        if i == "à":
            liste_vide.append("a")
        if i == "ù":
            liste_vide.append("u")
        if i in alphabet:
            liste_vide.append(i)
    return liste_vide


def transformationPhrase(phrase):
    phraseTransformee = list(phrase)
    for car in phraseTransformee:
        if car not in alphabet:
            phraseTransformee.remove(car)
    return phraseTransformee


def palindromePhrase(phrase):
    if palindromeMot(nettoyage(phrase)):
        print("C'est un palindrome")
    else:
        print("Ce n'est pas un palindrome")


print(palindromePhrase("ce reptile lit perec"))
