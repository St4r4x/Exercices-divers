# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 08:59:53 2022

@author: st4r4x
"""

X = [10, 12, 5, 0, 3]


def maximum(tableau):
    if len(tableau) == 1:
        return tableau[0]
    elif tableau[1] > tableau[0]:
        tableau.pop(0)
        return maximum(tableau)
    else:
        tableau.pop(1)
        return maximum(tableau)


print(maximum(X))
