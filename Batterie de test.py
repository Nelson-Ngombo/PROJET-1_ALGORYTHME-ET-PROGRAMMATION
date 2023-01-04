# -*- coding: utf-8 -*-
import random
import time as tm
import main as tp1
class test:
    start= tm.time()
    try: 
        
         print("calcul du perimetre et de la surface du rectangle")
         a=float(random.randint(1,50))
         b=float(random.randint(1,50))
       
         c=tp1.rectangle(a,b)
         print("le perimetre est : ",c.perimetre())
         print("la surface est : ",c.surface())
        
        
         print("calcul du perimetre et de la surface d'un triangle")
         a=float(random.randint(1,50))
         b=float(random.randint(1,50))
         c=float(random.randint(1,50))
         d=float(random.randint(1,50))
         tr=tp1.triangle(a,b,c,d)
         print("le perimetre est : ",tr.perimetre())
         print("la surface est : ",tr.surface())
        
        
         print("calcul du perimetre et de la surface d'un cercle")
         a=float(random.randint(1,50))
    
         cer=tp1.cercle(a)
         print("le perimetre est : ",cer.perimetre())
         print("la surface est : ",cer.surface())

         print("calcul du perimetre et de la surface du carré ")
         a=float(random.randint(1,50))
    
         car=tp1.carre(a)
         print("le perimetre est : ",car.perimetre())
         print("la surface est : ",car.surface())
        
        
         print("calcul du perimetre et de la surface d'un triangle rectangle")
         a=float(random.randint(1,50))
         b=float(random.randint(1,50))
         c=float(random.randint(1,50))
    
         triRect=tp1.triangle_rectangle(a,b,c)
         print("le perimetre est : ",triRect.perimetre())
         print("la surface est : ",triRect.surface())
    except:
        print("veuiller verifier si toutes vos valeurs sont numeriques ")
    end=tm.time()
    temps= end-start
    
    print("le temps d'execution est : ",temps)
    
    
    
    