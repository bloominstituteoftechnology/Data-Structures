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
    
    def __str__(self):
        ll = ""
        node = self.head
        while node != None:
            ll += f"{str(node.value)}, "
            node = node.next
        return ll[:-2]
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head:
            temp = self.head
            self.head = ListNode(value, None, temp)
            temp.prev = self.head
        else:
            self.head = ListNode(value, None, None)
            self.tail = self.head
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        old_head = self.head 
        new_head = old_head.next
        if new_head:
            new_head.prev = None
            self.head = new_head
        else:
            self.head, self.tail = None, None
        self.length -= 1
        return old_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail:
            new_tail = ListNode(value, self.tail, None)
            self.tail.next = new_tail
            self.tail = new_tail
            self.length += 1
        else:
            self.add_to_head(value)
        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        old_tail = self.tail
        if old_tail == None:
            return None
        new_tail = old_tail.prev
        if new_tail:
            new_tail.next = None
            self.tail = new_tail
        else:
            self.head, self.tail = None, None
        self.length -= 1
        return old_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        temp = self.head
        self.head = node
        self.head.next = temp
        self.head.prev = None
        temp.prev = self.head
        self.length += 1
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node
        self.length += 1
        
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node.prev == None:
            self.remove_from_head()
        elif node.next == None:
            self.remove_from_tail()
        else:
            prev, next = node.prev, node.next
            prev.next, next.prev = next, prev
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_val = float("-inf")
        node = self.head
        while node != None:
            if node.value > max_val:
                max_val = node.value
            node = node.next
        return max_val

# ll = DoublyLinkedList()

# for n in [ 2, 3, 5, 9 , 1]:
#     ll.add_to_tail(n)

# print(ll)

# ll.remove_from_head()

# print(ll)

# x = ll.remove_from_tail()

# print(f"removed val: <{x}> ", ll)

# x = ll.remove_from_head()

# print(f"removed val: <{x}> ", ll)

# ll.add_to_head(2)

# print(ll)

# ll.delete(ll.head.next)

# print(len(ll))
node = ListNode(1)

ll = DoublyLinkedList(node)

ll.remove_from_tail()

ll.add_to_tail(33)

print(len(ll))