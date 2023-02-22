# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 03:03:32 2023

@author: ASUS
"""

def max_et_min(tab, n=0):
    if n == len(tab)-1:
        return tab[n], tab[n]
    else:
        m, M = max_et_min(tab, n+1)
        return min(tab[n], m), max(tab[n], M)
 
import random
liste=[random.randint(0,1000) for i in range(100)]
print(liste)
print("les elements min et max sont : ",max_et_min(liste))

