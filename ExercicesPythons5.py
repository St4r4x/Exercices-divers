# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:27:32 2022

@author: st4r4x
"""


# fonction qui fait un tableau avec les table de multiplication de 1 à n
def tableMultiplication(n):
    start = 0
    stop = 10
    i = 1
    table = []
    while i <= n:
        table_multi = list(range(start, stop*i, i))
        table.append(table_multi)
        i += 1
    print(table)


def multiplication(x):
    res = []
    for i in range(x):
        line = []
        for j in range(x):
            line.append(i*j)
        res.append(line)
    return res


tableauMultiplication = multiplication(10)
