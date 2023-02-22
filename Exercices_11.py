# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 23:09:57 2023

@author: ASUS
"""
import random
import time
def recherche_max(tab,n):
    if n == len(tab)-1:
        return tab[n]
    return max(tab[n], recherche_max(tab, n+1))
def le_max(tab):
    return recherche_max(tab, 0)



d=time.time_ns()

liste=[random.randint(0,1001) for i in range(100)]
print(liste)
print("l'element max est : ",le_max(liste))

f=time.time_ns()

print("le temps d'execution en nano_seconde est :",f-d)