"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
tips: 
change pointers 
update new head node 
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
        if self.head is None: 
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1
        else:
            new_node = ListNode(value, next = self.head)
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
            
            
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    a)    Change the head pointer to next of current node (head here).
    b)    Change the previous pointer of next node to current node previous.
    """
    def remove_from_head(self):
        if not self.head:
            return None
        # else:
        #     value = self.head.value
        #     self.delete(self.head)
        #     return value
        # or 
        # store value into head 
        replacement = self.head.value
        self.length -= 1
        
        # delete current head value
        if self.head.next != None:
            # set to the left "self.head.next.prev" to NONE
            self.head.next.prev = None
            # set self.head to "self.head.next"
            self.head = self.head.next 
        else:
            # set head back to none
            self.head = None
            # ste tail to none
            self.tail = None
        
        return replacement
        
        
        
            
            
           
        
            

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value): 
        new_node = ListNode(value)
        # # new_node.prev = self.tail
        # self.tail.next = new_node
        # self.tail = new_node
        # self.length += 1
        # return self
        # self.add_to_head(value)
        
        if not self.head and not self.tail:
           
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            
        
        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # delete
        # save the value we deleted 
        # add_to_head(value)
         # check empty list
        del_ = self.tail
        if del_ == None:
            return None
        new_node = del_.prev
        if new_node:
            new_node.next = None
            self.tail = new_node
        else:
            self.head = None
            self.tail = None
            self.length -= 1
        return del_.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # value = node 
        # self.delete(node)
        # self.add_to_head(node)
        if node is self.head:
            # check if if node is already the head
            return
        else:
            # self.delete(node)
            # save new value 
            node.next = self.head
            node.prev = None
            self.head.prev = node
            
            self.head = node 
            
            # or
            # self.head.prev = node
            # node.next = self.head
            # node.prev = None
            # self.head = node
            # self.length += 1
        
        
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
        # updates the current node pointer to point to the next node
        # node.self.head.prev.next = node.next
        # # look at what comes after 'node' and set its 'prev' pointer = 
        # # to 'node's 'prev' pointer
        # node.cur_node.next.prev = node.prev
        # self.length -= 1
        if not self.head and not self.tail:
            return
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        
        # elif node is self.head:
        #     self.head = self.head.next
        #     self.head.prev = None
        #     self.length -= 1
        # elif node is self.tail:
        #     self.tail = self.tail.prev
        #     self.tail.next = None
        #     self.length -= 1
        # elif self.head == self.tail:
        #      self.head = None
        #      self.tail = None
        #      self.length -= 1
        else: 
            node.prev.next = node.next 
            node.next.prev = node.prev
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        #  keep track of current max_value 
        cur_node = self.head
        cur_max = self.head.value
        
        # loop through 
        while cur_node is not None:
            # compare current max_value with each value 
            if cur_node.value > cur_max:
                # update 
                cur_max = cur_node.value
            cur_node = cur_node.next
        # return max  
        return cur_max

    def print_list(self):
        l = []
        current = self.head
        while current:
            l.append(current.value)
            current = current.next
        return l
    
    

dll = DoublyLinkedList()

dll.add_to_head(1)
dll.add_to_head(2)
dll.add_to_head(3)
dll.add_to_head(4)
dll.add_to_head(5)

print(dll.print_list())