class LinkedStack:  # utilisation d'une chaine de liste pour le stockage
    class _Node:    # classe de Noeud imbriqué
        __slots__ = '_element', '_next'

        def __init__(self, element, next):   #définit l' état initial de la pile
            self._element = element
            self._next = next

    def __init__(self):       # création d'une pile vide
        self._head = None
        self._size = 0

    def __len__(self):       #Renvoie le nombre d'elements dans la pile

        return self._size

    def is_empty(self):         #Renvoie True si la pile est vide c'est à dire on verifie si la pile est vide

        return self._size == 0

    def push(self,element):           #Ajoute l'element donne en parametre en tete de la pile

        self._head = self._Node(element, self._head)
        self._size +=1

    def pop(self):       #Efface et donne en retour l'element au sommet de la liste
                         #Leve une exception si la liste est vide

        try:
            self.is_empty()
            answer = self._head._element
            self._head = self._head._next
            self._size = self._size - 1
            return answer
        except:
            print('Liste vide')

    def top(self):           #Renvoie l'element en haut de la pile sans l'effacer
                             #Leve une exception si la liste est vide
        try:
           self.is_empty()
           return self._head._element
        except:
            print('Liste vide')



