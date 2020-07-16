"""
### Doubly Linked Lists
 * The `ListNode` class, which represents a single node in the doubly-linked list, has already been implemented for you. Inspect this code and try to understand what it is doing to the best of your ability.
 * The `DoublyLinkedList` class itself should have the methods: `add_to_head`, `add_to_tail`, `remove_from_head`, `remove_from_tail`, `move_to_front`, `move_to_end`, `delete`, and `get_max`.
   * `add_to_head` replaces the head of the list with a new value that is passed in.
   * `add_to_tail` replaces the tail of the list with a new value that is passed in.
   * `remove_from_head` removes the head node and returns the value stored in it.
   * `remove_from_tail` removes the tail node and returns the value stored in it.
   * `move_to_front` takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down. 
   * `move_to_end` takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up. 
   * `delete` takes a reference to a node in the list and removes it from the list. The deleted node's `previous` and `next` pointers should point to each afterwards.
   * `get_max` returns the maximum value in the list. 
 * The `head` property is a reference to the first node and the `tail` property is a reference to the last node.
"""

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
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if(self.head):
            current = self.head
            if self.head is self.tail:
                self.tail = None
            self.head = current.next
            self.length -= 1
            return current.value


    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if(self.head):
            current = self.tail
            while(current.next):
                current = current.next
            new_node.prev = current
            current.next = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.length += 1
            self.head = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        curr_tail = self.tail
        if curr_tail.prev:
            self.tail = curr_tail.prev
            new_tail = curr_tail.prev
            new_tail.value = None
        else:
            self.tail = None
            self.head = None
        self.length -= 1
        return curr_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        current = self.head
        while current != node:
            current = current.next
        if current.prev:
            before = current.prev
            before.next = current.next
        if current.next:
            after = current.next
            after.prev = current.prev

        prev_head = self.head
        prev_head.prev = current
        current.next = prev_head
        current.prev = None
        self.head = current
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        current = self.head
        while current != node:
            current = current.next
        if current.prev:
            before = current.prev
            before.next = current.next
            if node == self.tail:
                self.tail = before
        if current.next:
            after = current.next
            after.prev = current.prev
            if node is self.head:
                self.head = after
        
        prev_tail = self.tail
        prev_tail.next = current
        current.prev = prev_tail
        current.next = None
        self.tail = current 

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current = self.head
        while current != node:
            current = current.next
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        if current.prev:
            before = current.prev
            before.next = current.next
            if node == self.tail:
                self.tail = before
        if current.next:
            after = current.next
            after.prev = current.prev
            if node == self.head:
                self.head = after
        self.length -= 1

    


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        item = 0
        while current:
            if current.value > item:
                item = current.value
            current = current.next
        
        return item

