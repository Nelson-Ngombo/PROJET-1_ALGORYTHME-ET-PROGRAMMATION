import main as tp1
class test:
    try:
        
        print("calcul du perimetre et de la surface du rectangle")

        a=float(input("entrer la longueur : "))
        b=float(input("entrer la largeur : "))

        c=tp1.rectangle(a,b)

        print("le perimetre est : ",c.perimetre())
        print("la surface est : ",c.surface())
        print("calcul du perimetre et de la surface d'un triangle")

        a=float(input("entrer la hauteur : "))
        b=float(input("entrer le coté 1 : "))
        c=float(input("entrer le coté 2 : "))
        d=float(input("entrer le coté 3 : "))


        tr=tp1.triangle(a,b,c,d)

        print("le perimetre est : ",tr.perimetre())
        print("la surface est : ",tr.surface())
        print("calcul du perimetre et de la surface d'un cercle")
        a=float(input("entrer le rayon : "))
        cer=tp1.cercle(a)
        print("le perimetre est : ",cer.perimetre())
        print("la surface est : ",cer.surface())
        
        print("calcul du perimetre et de la surface du carré ")

        a=float(input("entrer la cote : "))
       

        car=tp1.carre(a)

        print("le perimetre est : ",car.perimetre())
        print("la surface est : ",car.surface())
        
        print("calcul du perimetre et de la surface d'un triangle rectangle")

        a=float(input("entrer la hauteur : "))
        b=float(input("entrer le coté 1 : "))
        c=float(input("entrer l'hypotenus' : "))
        


        triRect=tp1.triangle_rectangle(a,b,c)

        print("le perimetre est : ",triRect.perimetre())
        print("la surface est : ",triRect.surface())

    except:
        print("veuiller verifier si toutes vos valeurs sont numeriques ")
