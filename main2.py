# PROGRAMMATION ORIENTE OBJETS AVEC COMME PILIER LE POLYMORPHISME
class rectangle:
    def __init__(self,haut,larg):
        self.haut=haut
        self.larg=larg
        
    def surface(self):
        return self.haut*self.larg
    
    def perimetre(self):

        return (self.haut+self.larg)*2
