# PROGRAMMATION ORIENTE OBJETS AVEC COMME PILIER LE POLYMORPHISME
class rectangle:
    def __init__(self,haut,larg):
        self.haut=haut
        self.larg=larg
        
    def surface(self):
        return self.haut*self.larg
    
    def perimetre(self):

        return (self.haut+self.larg)*2
import math
class cercle:
    def __init__(self,rayon):
        self.rayon=rayon
        
        
    def surface(self):
        return math.pi*self.rayon**2
        
    def perimetre(self):
        return 2*math.pi*self.rayon

class triangle:
    def __init__(self,haut,cote1,cote2,cote3):
        self.haut=haut
        self.cote1=cote1
        self.cote2=cote2
        self.cote2=cote2

    def surface(self):
        return self.haut*self.cote1/2
    
    def perimetre(self):
        return (self.cote1+self.cote2+self.cote3)
class carre:
    def __init__(self,cote):
        self.cote=cote
        
        
    def surface(self):
        return self.cote**2
    
    def perimetre(self):
        return self.cote*4
