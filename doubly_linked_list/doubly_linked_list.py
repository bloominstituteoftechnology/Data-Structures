"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    # def __repr__(self):

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


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # first, let's get the new_node connected as the current head's prev
            self.head.prev = new_node
            # then, get that new_node's next connector latched onto the current head
            self.head.prev.next = self.head
            # then, you change the head to the new_node
            self.head = new_node
            # increment length
            self.length += 1

    def remove_from_head(self):
        value_removed = None
        if self.head is None and self.tail is None:
            return None
        if self.head is self.tail:
            value_removed = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
        
        else:
            value_removed = self.head.value
            self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1

            # lol, what even happens to the old head? i think its just floating there
        return value_removed

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length += 1
            #print(f"the tail is : {self.tail}")

    def remove_from_tail(self):
        value_removed = None
        if self.head is None and self.tail is None:
            return None

        if self.head is self.tail:
            value_removed = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            value_removed = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        return value_removed

    def move_to_front(self, node):
        current_node = node
        if node is self.head:
            print("node is already at front")
            
        elif node is self.tail:
            self.remove_from_tail()
            self.add_to_head(current_node.value)
        else:
            # get rid of it
            self.delete(node)
            self.add_to_head(current_node.value)
        

    def move_to_end(self, node):
        current_node = node
        if node is self.tail:
            print("node is already at end, dumbo")
            
        elif node is self.head:
            # we need special functions for heads and tails
            self.remove_from_head()
            self.add_to_tail(current_node.value)
        else:
            # get rid of it
            self.delete(node)
            self.add_to_tail(current_node.value)
        


    def delete(self, node):
        if self.head is node:
            self.remove_from_head()
        elif self.tail is node:
            self.remove_from_tail()
        else:
            self.length -= 1
            node.delete()

    def get_max(self):
        # traverse through total array, add all values
        max_value = self.head.value
        current_node = self.head
        while current_node is not self.tail.next:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value
