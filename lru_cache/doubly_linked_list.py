"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, key, value):
        # wrap the given value in a ListNode
        new_node = ListNode(key, value, None, None)
        self.length += 1
        # handle if list has a head
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        # handle if list has no head
        else:
            self.tail = new_node

        self.head = new_node



    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    # def remove_from_tail(self):
    #     key = self.tail.keyremove_from_tail

        # return key
    def remove_from_tail(self):
        # empty list
        if not self.head:
            print("Nothing to see here")
            return None
        
        # List with one node
        elif self.head == self.tail:
            delkey = self.head.key
            self.head = None
            self.tail = None
            self.length -= 1
            return delkey

        # List with more that one node
        else:
            checknode = self.head
            while checknode.next != self.tail:
                checknode = checknode.next
            
            delkey = self.tail.key
            self.tail.delete()
            self.tail = checknode
            self.length -= 1
            return delkey

    def set_tail(self):
        checknode = self.head
        while checknode is not None:
            if checknode.next == None:
                self.tail = checknode

            checknode = checknode.next
        
        # self.tail = checknode

    #Removes the input node from its current spot in the List and inserts it as the new head node of the List.
    def move_to_front(self, node):
        # delete
        self.delete(node)
        # then add to front
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.length += 1
            


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        
        # if list is empty
        if not self.head:
            print('I aint got nothing for you bro')
            return
        
        # if list has just one item
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        
        # we have at least two nodes, and the node we want to delete is the head
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
            self.length -= 1

        # we have at least two nodes and the node we want to delete is the tail
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            self.length -= 1
        
        else:
            node.delete()
            self.length -= 1
  