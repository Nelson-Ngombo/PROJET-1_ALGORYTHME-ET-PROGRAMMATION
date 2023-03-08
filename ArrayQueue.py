class Empty(Exception):
    pass
class ArrayQueue:

    def __init__(self):
        """Keep track of 3 things"""
        INIT_CAP = 10
        self._data = [None]*INIT_CAP
        self._front = 0
        self._n = 0

    def __len__(self):
        """Return number of elements in queue"""
        return self._n

    def __str__(self):
        return str(self._data)
        #ix_sequence = [(self._front+i)%(len(self._data)) for i in range(self._n)]
        #contents = ",".join([str(self._data[ix]) for ix in ix_sequence])
        #return "[" + contents + "]"

   #####################
   # Note: start with the
   # simple stuff. __getitem__,
   # __len__, __init__, __str__, etc.

    def is_empty(self):
        """Returns true if no elements in queue"""
        return self._n==0

    def dequeue(self):
        """Pop an item from the front of the queue (inch the front pointer along)"""
        if(self.is_empty()):
            raise Empty("oops, empty queue")

        dafront = self._data[self._front]

        self._data[self._front]=None # clean up
        self._front = (self._front+1)%(len(self._data)) # update front pointer
        self._n -= 1

        # Really, we need to resize this thing to be smaller
        # when we remove stuff from it.
        # If it is too big by a quarter, chop it in half.
        if(self._n < len(self._data)//4):
            self.resize( len(self._data)//2 )

        return dafront


    def enqueue(self, e):
        """Add an item to the back of the queue"""
        if(self._n==len(self._data)):
            self.resize(2*self._n)

        insert_index = (self._front + self._n )%(len(self._data))
        self._data[insert_index] = e
        self._n += 1

    def resize(self,newsize):
        """Redimensionnez et déplacez tout vers l'avant"""
        old = self._data
        walk = self._front
        self._data = [None]*newsize
        for k in range(self._n):
            self._data[k] = old[walk]
            walk = (walk+1)%len(old)
        self._front = 0

    def first(self):
        return self._data[self._first]
    


ar=ArrayQueue()
print(ar.is_empty())
ar.enqueue(1)                   # ajout des elements
ar.enqueue(2)
print(ar.is_empty())
print(len(ar))
ar.resize(3)