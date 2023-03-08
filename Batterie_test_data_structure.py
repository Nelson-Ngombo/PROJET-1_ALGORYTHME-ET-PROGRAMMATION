# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:57:01 2023

@author: ASUS
"""
import LinkedStack as lst
import LinkedQueue as Lq
import CircularQueue as Cq
print("test pour linkstack \n___________________________________\n")
ls= lst.LinkedStack()

print(ls.is_empty())               #verifions si la pile est effectivement vide
print('Top Element:', ls.top())    # verifions s'il n'y a aucun top element
print('Popped:', ls.pop())         # verifions s'il n'ya aucun popped element

ls.push(10)   # ajout des elements 
ls.push(20)
ls.push(30)
ls.push(40)


print(ls.is_empty())      # verifions si le panier n'est pas vide
print(len(ls))            #retourne le nombre d'element ajoutÃ©


ls.pop()                  # retrait d'element au sommet de pile




print('Popped:', ls.pop()) # supprime et retourne le dernier element ajoutÃ©

print(len(ls))             # retourne le nombre d'elements restant


ls.push(70)                 #ajout d'un nouvel element

print('Top Element:', ls.top())  # retourne le dernier element ajoutÃ©
print('Popped:', ls.pop()) 

print("test pour linkqueue \n___________________________________\n")


lq=Lq.LinkedQueue()
print(lq.is_empty())           #verifions si la file est effectivement vide
print(lq.first())              # verifions s'il n'ya aucun premier element dans la file

lq.enqueue(1)                   # ajout des elements
lq.enqueue(2)
lq.enqueue(3)
lq.enqueue(4)
lq.enqueue(5)



print(lq.is_empty())                  # verifions si la file n'est pas vide
print(len(lq))                        #retourne le nombre d'element ajouté

lq.dequeue()                           # retrait progressive des elements dans la file
lq.dequeue()


print(len(lq))                        # retourne le nombre d'elements restant
print(lq.first())                      # retourne le premier element de la file restante

print("test pour linkqueue \n___________________________________\n")
obj = Cq.MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()




