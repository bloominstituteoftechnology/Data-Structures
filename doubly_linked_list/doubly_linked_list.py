"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
          new_node = ListNode(value, None, None)
          self.length += 1
          if not self.head and not self.tail:
              self.head = new_node
              self.tail = new_node
          else:
              new_node.next = self.head
              self.head.prev = new_node
              self.head = new_node    
          return new_node
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
         value = self.head.value
         self.delete(self.head)
         return value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length  +=1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node    
        return new_node    
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.head = node
                
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.tail is node:
            return self.tail
        value = node.value
        self.delete(node)
        self.add_to_tail(value)
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            node.delete()
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
         

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        cur_node = self.head
        cur_max = self.head.value 
        while cur_node is not None:
           if cur_node.value > cur_max:
              cur_max =  cur_node.value
              cur_node = cur_node.next 
        return  cur_max   
    
dl = DoublyLinkedList()
dl.add_to_tail(9)
dl.add_to_tail(8)
print('MAX',dl.get_max())
    
    