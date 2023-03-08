class LinkedQueue: # implementation de file d'attente pour le stockage <<FIFO>>

    class _Node:               # classe de Noeud imbriqué

        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):     # creation d'une file d'attente

        self._head = None
        self._tail = None
        self._size =0

    def __len__(self):     # retourne le nombre d'element dans la file d'attente

        return self._size

    def is_empty(self):           # retourne vrai si la file est vide

        return self._size==0

    def first(self):      # retourne l'element au devant de la file sans le supprimer

        try:
            self.is_empty()
            return self._head._element

        except:
            print("file vide")

    def enqueue(self,element):
        newest=self._Node(element,None)
        if self.is_empty():
                self._head=newest
        else:
                self._tail._next=newest
        self._tail=newest
        self._size += 1

    def dequeue(self):
        try:
            self.is_empty()
            answer= self._head._element
            self._head=self._head._next
            self._size -= 1
            self._tail = None
            return answer
        except:
            print("file vide")



