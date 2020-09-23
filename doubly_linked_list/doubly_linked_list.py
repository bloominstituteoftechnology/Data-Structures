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
        newnode = ListNode(value)
        if not self.head and not self.tail:
            self.head = newnode
            self.tail = newnode
            self.length += 1
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None
        elif self.head == self.tail:
            value  = self.head.value
            self.head = None
            self.tail = None
            return value
        else:
            value  = self.head.value
            self.head = self.head.next
            return value
        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        newnode = ListNode(value)
        if not self.head and not self.tail:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
            

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return None
        elif self.head == self.tail:
            value  = self.head.value
            self.head = None
            self.tail = None
            return value
        else:
            value  = self.tail.value
            self.tail = self.tail.prev
            return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        currentnode = self.head
        if self.head.value == node:
            print('already at the head of the linked list!')
        elif self.tail.value == node:
            value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            newnode = ListNode(value)
            self.head.prev = newnode 
            newnode.next = self.head
            self.head = newnode
            
        else:
            while currentnode.value != node:
                currentnode = currentnode.next
            value = currentnode.value
            nextnode = currentnode.next
            prevnode = currentnode.prev
            prevnode.next = nextnode
            nextnode.prev = prevnode
            newnode = ListNode(value)
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        
        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        currentnode = self.head
        if self.tail.value == node:
            print('already at the end of the linked list!')
        elif self.head.value == node:
            value = self.head.value
            newnode = ListNode(value)
            self.head = self.head.next 
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        else:
             while currentnode.value != node:
                currentnode = currentnode.next
             value = currentnode.value
             nextnode = currentnode.next
             prevnode = currentnode.prev
             prevnode.next = nextnode
             nextnode.prev = prevnode
             newnode = ListNode(value)
             self.tail.next = newnode
             newnode.prev = self.tail
             self.tail = newnode

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        currentnode = self.head
        while currentnode.value != node:
            currentnode = currentnode.next
        currentnode.value = None
        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        values = []
        currentnode = self.head
        while currentnode.next != None:
            values.append(int(currentnode.value))
            currentnode = currentnode.next
        values.append(int(currentnode.value))
        return max(values)

    def view(self):
        list = []
        currentnode = self.head
        while currentnode != self.tail:
            list.append(str(currentnode.value))
            currentnode = currentnode.next
        list.append(str(currentnode.value))
        return '-->'.join(list)

LL = DoublyLinkedList()
LL.add_to_head(2)
LL.add_to_head(4)
LL.add_to_head(6)
print(LL.view())
LL.move_to_end(2)
# LL.remove_from_tail()
print(LL.view())
LL.move_to_end(6)
print(LL.view())
LL.move_to_end(6)
print(LL.view())
LL.move_to_end(6)
LL.move_to_end(4)
print(LL.view())
LL.move_to_front(4)
print(LL.view())
LL.move_to_front(4)
print(LL.view())
LL.move_to_front(2)
print(LL.view())
print(LL.get_max())
LL.delete(4)
print(LL.view())
LL.remove_from_head()
LL.remove_from_tail()
print(LL.view())
LL.add_to_tail(2)
print(LL.view())
# LL.remove_from_tail()
# print(LL.view())