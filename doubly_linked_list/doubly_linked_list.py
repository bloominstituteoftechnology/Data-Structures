"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
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
    
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #create new node:
        new_node = ListNode(value, None, None)
        #check if DLL is empty:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length = self.length + 1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #Make sure list is not empty
        if not self.head and not self.tail:
            return None
        #check if List only has one node (getting rid of head should make it None)
        

        elif self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return value
        else:
            value = self.head.value
            current_next = self.head.next
            current_previous = self.head.prev
            self.head = current_next
            self.head.prev = current_previous
            self.length = self.length - 1
            return value
            #self.head.next = 

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value): 
        #make new ListNode
        new_node = ListNode(value)
        #check if list is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
        elif self.head == self.tail:
            self.head.next = new_node
            self.tail = new_node
            self.tail.prev = self.head
            self.tail.next = None
            self.length = self.length + 1
        else:
            current_tail = self.tail
            current_tail.next = new_node
            self.tail = new_node
            self.tail.prev = current_tail
            self.tail.next = None
            self.length = self.length + 1




            

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        #check if it is empty and check if there's only one
        if not self.head and self.tail:
            return None
        elif self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return value
        else:
            value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            return value

        

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    #tail.prev = another node tail.next = NOne tail.value =value
    #head.prev =None head.next = node head.value = value
    #tail.next = head head.prev = tail 
    def move_to_front(self, node):
        # node = ListNode(value) <= why does that not work????
        if not self.head and self.tail:
            return None
        elif self.head == self.tail:
            return None
        elif self.length == 2:
            current_head = self.head
            current_tail = self.tail

            self.head = current_tail
            self.tail = current_head
            self.head.prev = None
            self.head.next = self.tail
            self.tail.prev = self.head
            self.tail.next = None
        else:
            ##removes node from current place in list:
            node.prev.next = node.next
            node.next.prev = node.prev
            ## puts node in front of list:
            #set current_head (before insertion)
            current_head = self.head
            #setting new node to head
            self.head = node
            current_head.prev = self.head
            self.head.prev = None
            self.head.next = current_head





            
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        #need to make sure it is not empty and there isn't just one
        if not self.head and self.tail:
            return None
        elif self.head == self.tail:
            return None
        elif self.length == 2:
            current_head = self.head
            current_tail = self.tail

            self.head = current_tail
            self.tail = current_head
            self.head.prev = None
            self.head.next = self.tail
            self.tail.prev = self.head
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

            current_tail = self.tail
            self.tail = node
            self.tail.prev = current_tail
            self.tail.next = None
            current_tail.next = self.tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head is node:
            current_head = self.head
            self.head = current_head.next
            self.head.prev = None
            self.length -= 1
        elif self.tail is node:
            current_tail = self.tail
            self.tail = current_tail.prev
            self.tail.next = None
            self.length -= 1
        else:
            # self.delete(node)
            node.delete()
            self.length -= 1
            #why no decrement within this block????

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head and self.tail:
            return None

        max_value = self.head.value
        # reference to our current node as we traverse the list
        current = self.head.next
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.value
            # update the current node to the next node in the list
            current = current.next
        return max_value