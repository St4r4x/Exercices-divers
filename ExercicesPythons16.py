# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:10:40 2022

@author: st4r4x
"""
phrase = "¿Hola que tal?"


def longueur(phrase):
    if phrase == "":
        return 0
    else:
        return 1+longueur(phrase[1:])


print(longueur(phrase))
