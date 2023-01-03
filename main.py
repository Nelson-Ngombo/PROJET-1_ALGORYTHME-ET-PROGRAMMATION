from math import pi
from abc import ABCMeta, abstractmethod 

class forme_geometrique(metaclass=ABCMeta):
    
    @abstractmethod
    
    def surface(self):
        pass  
    def perimetre(self):
        pass
class rectangle(forme_geometrique):
    
    def __init__(self,hauteur,larg):
        self.hauteur=hauteur
        self.larg=larg
    def surface(self):
        return self.hauteur*self.larg
    
    def perimetre(self):
        return (self.hauteur+self.larg)*2
    
# 'jai importé le module math pour utiliser "pi" 

class cercle(forme_geometrique):
    def __init__(self, rayon):
        self.rayon=rayon
    def surface(self):
        return pi*self.rayon**2
    def perimetre(self):
        return 2*pi*self.rayon
    
class triangle(forme_geometrique):
    def __init__(self,hauteur,cote1,cote2,cote3):
        self.hauteur=hauteur
        self.cote1=cote1 
        self.cote2=cote2
        self.cote3=cote3
    def surface(self):
        resultat=self.hauteur*self.cote1/2
        return resultat
    def perimetre(self):
        return self.cote1+self.cote2+self.cote3

    #Ajoute la classe carre
