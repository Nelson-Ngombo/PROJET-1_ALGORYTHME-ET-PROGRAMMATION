class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        self.list = list() # Initialize a list (Python's built-in dynamic array) to store the items
        if iterable is not None:
            for item in iterable:
                self.push(item)
    
    def push(self, item):
        """"Insert given item on top of stack
        Running time: O(1) unless reached maximum array size, then exceptionally O(n)"""
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        last_item_idx = len(self.list) - 1
        return None if last_item_idx < 0 else self.list[last_item_idx]
    
    def pop(self):
        """Remove and return top item, if any, or raise ValueError if empty
        Running time: O(1) since only removing last item, all other items stay where they are"""
        if self.peek() == None:
            raise ValueError("list is empty")
        else:
            return self.list.pop()
a=ArrayStack()
a.push(1)
a.push(2)
a.peek()
a


