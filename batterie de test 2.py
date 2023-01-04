from main2 import*
import random

import time as tm
class formegeometrique:
    
 
    start=tm.time()

    print("vous aller calculer le perimetre et la surface du rectangle")
    a=float(random.randint(1,50))
    b=float(random.randint(1,50))

    rect=rectangle(a,b)
    print("la surface du rectangle : ",rect.surface())
    print("la perimetre du rectangle : ",rect.perimetre())
    

    print("vous aller calculer le perimetre et la surface du triangle")
    a=float(random.randint(1,50))
    b=float(random.randint(1,50))
    c=float(random.randint(1,50))
    d=float(random.randint(1,50))
    tri=triangle(a,b,c,d)
    print("la surface du triangle est :  ",tri.surface())
    print("la perimetre du rectangle est : ",tri.perimetre())
    
        
    a=float(random.randint(1,50))
     
    
    cer=cercle(a)
    print("la surface du cercle : ",cer.surface())
    print("la perimetre du cercle : ",cer.perimetre())
     
        
        
    
    print("calcul de la surface et du perimetre d'un carré ")
    a=float(random.randint(1,50))
        
        
    car=carre(a)
    print("la surface du carré est :  ",car.surface())
    print("la perimetre du carré est : ",car.perimetre())
    
    
    print("vous aller calculer le perimetre et la surface du triangle_rectangle")
    a=float(random.randint(1,50))
    b=float(random.randint(1,50))
    c=float(random.randint(1,50))
        
    
    tri=triangleRectangle(a,b,c)
    print("la surface du triangle est :  ",tri.surface())
    print("la perimetre du rectangle est : ",tri.perimetre())    
    
    end=tm.time()
    
    temps= end-start
    
    
    print("le temps d'execution est ", temps)
