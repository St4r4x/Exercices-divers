# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:21:41 2022

@author: st4r4x
"""


def sapinNoel(hauteur, cpt):
    if hauteur == 0:
        return False
    print((" " * hauteur), ("*" * cpt))
    cpt += 2
    return sapinNoel(hauteur-1, cpt)


sapinNoel(int(input("Saisir la hauteur du triangle : ")), 1)
