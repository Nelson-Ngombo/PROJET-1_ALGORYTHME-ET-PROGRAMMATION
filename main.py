
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
