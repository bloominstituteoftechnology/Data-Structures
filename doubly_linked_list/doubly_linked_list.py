"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
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


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList():
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    @property
    def empty(self):
        return self.length == 0
    @property
    def single(self):
        # return  not self.empty and (self.head.next is None)  
        return self.length == 1

    def add_to_head(self, value):
        if self.head is None and self.tail is None:
            l = ListNode(value)
            self.head = l
            self.tail = l
        else:
            assert self.head is not None, 'logic error'
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1


    def remove_from_head(self):
        assert not self.empty, "can't removed_from_head for empty DoublyLinkedList"
        self.head.delete()
        value = self.head.value
        if self.single:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next 
        self.length -= 1          
        return value

        

    def add_to_tail(self, value):
        if self.head is None and self.tail is None:
            l = ListNode(value)
            self.head = l
            self.tail = l
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def remove_from_tail(self):
        assert not self.empty, "can't removed_from_tail for empty DoublyLinkedList"
        value = self.tail.value
        self.tail.delete()
        if self.single:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
        self.length -= 1
        return value
        


    def move_to_front(self, node):
        if self.single or self.empty:
            return   
    

        if node is None:
            return

        if node == self.tail:
            self.tail = node.prev

        node.delete()
  
        self.head.insert_before(node.value)
        self.head = self.head.prev




    def move_to_end(self, node):
        if self.single or self.empty:
            return

        if node is None:
            return

        if node == self.head:
            self.head = self.head.next

        node.delete()

        self.tail.insert_after(node.value)
        self.tail = self.tail.next

    def delete(self, node):
        assert not self.empty, "can't delete from empty linked list"
        if self.single : # node is the only one              
            self.head = None
            self.tail = None
            node.delete()
            self.length = 0
            return

        if self.tail == node:
            self.tail = node.prev

        if self.head == node:  
            self.head = node.next

        node.delete()
        self.length -= 1

    def get_max(self):
        if self.empty:
            return None
        r = self.head
        max = r.value
        while r.next != None:
            r = r.next
            if r.value > max:
                max = r.value            
        return max
                
        
