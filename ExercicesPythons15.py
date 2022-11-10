# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 13:46:16 2022

@author: st4r4x
"""


def echo(n):
    if n > 0:
        print("echo")
        echo(n-1)
    else:
        print("Plus d'écho")


echo(3)
