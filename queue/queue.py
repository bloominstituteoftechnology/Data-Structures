  
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 
1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue? --- The popping of the element with a list is at the 
   front of the list and when using a linked_list it is at the head.  With a list elements 
   then need to be shifted down becuase the element zero was removed.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Node:
    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value



# The linked list will use the nodes and then will make the linked list

class LinkedList():
    def __init__(self):
        self.head = None 
        self.tail = None
        self.length = 0  

    def add_to_tail(self, value):
        new_node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1


    def add_to_head(self, value):
        new_node = Node(value=value)
        self.length += 1
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def remove_head(self):
        """
            Function will return The head value.  If there is no value then 
            it will return None
        """
        if self.length == 0:
            return None
        theValue = self.head.value
        new_head = self.head.next_node
        self.head = new_head
        if self.length == 1:
            self.tail = None
        self.length -= 1

        return theValue


    def contains(self, searchValue):
        if self.length == 0:
            return False
        else:
            theNode = self.head 
            
            while theNode != None:
                if theNode.value == searchValue:
                    return True
                else:
                    theNode = theNode.next_node
            return False

    
    def get_max(self):
        
        if self.length == 0:
            return None
        val = self.head.value
        node = self.head
        while True:
            if node.value > val:
                val = node.value
          
            node = node.next_node
            if node == None:
                return val
           

class Queue:
    #  a list
    #def __init__(self):
    #    self.size = 0
    #    self.storage = []
#
    #  a linked list
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    
    def __len__(self):
        return self.size

    #  a list
    #def enqueue(self, value):
    #    self.storage.append(value)
    #    # add to the size 
    #    self.size += 1

    #  a linked list
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

        
    # a list
    #def dequeue(self):
    #    if self.size == 0:
    #        return None
    #    self.size -= 1
    #    return self.storage.pop(0)

    #  a linked list
    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()


