# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:54:20 2023

@author: ASUS
"""
from main2 import*

class formegeometrique:
    
    
    print("menu : ")
    print(" 1° rectangle \n 2° triangle \n 3° cercle \n 4° carré \n 5° triangle_rectangle")
    print("veuillez effectuer votre choix pour le calcul du perimetre et de la surface ")
    try:
    
        choix=int(input("choix : "))

        while (choix !=1 and choix !=2 and choix !=3 and choix !=4 and choix !=5 ):
            print("veuillez faire le bon choix")
            choix=int(input("choix : ")) 
    except:
        print("entrer des valeurs numerique")
    
    if choix==1:
        print("vous aller calculer le perimetre et la surface du rectangle")
        a=float(input("entrer la longueur : "))
        b=float(input("entrer la largeur : "))
        
        rect=rectangle(a,b)
        print("la surface du rectangle : ",rect.surface())
        print("la perimetre du rectangle : ",rect.perimetre())
        
    elif choix==2  :
        print("vous aller calculer le perimetre et la surface du triangle")
        a=float(input("entrer la hauteur : "))
        b=float(input("entrer le coté1 : "))
        c=float(input("entrer le coté2 : "))
        d=float(input("entrer le coté3 : "))

        tri=triangle(a,b,c,d)
        print("la surface du triangle est :  ",tri.surface())
        print("la perimetre du rectangle est : ",tri.perimetre())
    elif choix==3  :
        
        a=float(input("entrer le rayon : "))
    
        cer=cercle(a)
        print("la surface du cercle : ",cer.surface())
        print("la perimetre du cercle : ",cer.perimetre())
         
        
        
    elif choix==4:
        print("calcul de la surface et du perimetre d'un carré ")
        a=float(input("coté : "))
        car=carre(a)
        print("la surface du carré est :  ",car.surface())
        print("la perimetre du carré est : ",car.perimetre())
    
    elif choix==5  :
        print("vous aller calculer le perimetre et la surface du triangle_rectangle")
        a=float(input("entrer la hauteur : "))
        b=float(input("entrer le coté1 : "))
        c=float(input("entrer le hypotenus : "))
    
        tri=triangleRectangle(a,b,c)
        print("la surface du triangle est :  ",tri.surface())
        print("la perimetre du rectangle est : ",tri.perimetre())    
    
        
        
        
        