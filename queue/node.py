import time

class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list Node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next_node):
        self.next_node = new_next_node

    #okay :)

class LinkedList:
    def __init__(self):
    # reference to the head of the list
        self.head = None
    # reference to the tail of the list
        self.tail = None

    def add_to_tail(self, value):
        # init a node with a value of value
        new_node = Node(value, None)
        # check if there is no head(i.e., the list is empty)
        # if not self.head
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the tail
        else:
            # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self): 

        # Return None if there is no head (i.e. If the linked list is empty)
        if not self.head:
            return None

        # What if linked list has a singled element?

        # if self.head == self.tail # this actually wouldn't work if multiples of same values -- I take it back

        # If the head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure teh tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()

        # otherwise we have more than one element in our list
        else:
            value = self.head.get_value()
            self.head = self.head.get_next() # ty chelsea :)
            return value # chelsea's got my back, so does Elvis :-)

    def contains(self, value):
        # If linked list is empty, return False
        if not self.head:
            return False
        # Is this above part even needed because current is self.head and if this is None it won't run while loop
        else:
            current = self.head
            while current:
                if value == current.get_value():
                    return True
                else:
                    current = current.get_next()
        
            return False
                
    def add_to_head(self, value):
        # init a node with a value of value
        new_node = Node(value, None)

        # If the linked list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node 
    
        # If it has one item
        elif not self.head.get_next():
            new_node.set_next = self.head
            self.head = new_node
            
        # If it has 2 or more items
        else:
            prev_head = self.head
            self.head = new_node
            self.head.set_next(prev_head)
            



"""
Benchmark removing from the front of a list versus
removing from the front of a linked list
"""
if __name__ == '__main__':
  n = 100000

  l = [i for i in range(0, n)]
  ll = LinkedList()

  for i in range(0, n):
    ll.add_to_tail(i)
  
  start_time = time.time()
  for i in range(0, n):
    ll.remove_head()
  end_time = time.time()
  print(f'linked list remove from head runtime: {end_time - start_time} seconds')

  start_time = time.time()
  for i in range(0, n):
    l.pop(0)
  end_time = time.time()
  print(f'list pop from front runtime: {end_time - start_time} seconds')