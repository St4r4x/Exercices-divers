# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:11:24 2022

@author: st4r4x
"""
import string
alphabet = list(string.ascii_lowercase)


def palinMotRec(mot):
    if len(mot) in [0, 1]:
        return True
    elif mot[0] == mot[len(mot)-1]:
        return palinMotRec(mot[1:-1])
    else:
        return False


print(palinMotRec("kayak"))


def transformationPhrase(phrase):
    phrase = phrase.lower()
    listePhrase = []
    for i in phrase:
        if i == " ":
            i = 0
        if i == "," or i == "." or i == "?" or i == "!":
            i = 0
        if i == "é" or i == "è" or i == "ê":
            listePhrase.append("e")
        if i == "à":
            listePhrase.append("a")
        if i == "ù":
            listePhrase.append("u")
        if i in alphabet:
            listePhrase.append(i)
    return listePhrase


def palinPhraseRec(phrase):
    if len(phrase) in [0, 1]:
        return True
    elif phrase[0] == phrase[len(phrase)-1]:
        return palinPhraseRec(phrase[1:-1])
    else:
        return False

print(palinPhraseRec(transformationPhrase("Ce satrape repart à sec")))