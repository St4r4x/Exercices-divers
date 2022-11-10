# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:16:29 2022

@author: st4r4x
"""


def Fibo(n):
    if n in [0, 1]:  # si n egal à 0 ou 1, c'est vrai
        return n
    else:
        return Fibo(n-1)+Fibo(n-2)


print(Fibo(10))

liste_fibo = []
for i in range(10):
    liste_fibo.append(Fibo(i))
