# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 08:57:00 2022

@author: st4r4x
"""


def funPair(N):
    if N == 0:
        return True
    else:
        return funImpair(N-1)


def funImpair(N):
    if N == 0:
        return False
    else:
        return funPair(N-1)


print(funPair(5))
