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
    
# ajoute la classe triangle 