# linked_list

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        # check if there is no head
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        # is there a head
        if not self.head:
            return None

        # if head has no next, there is a single element in the linked list 
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None

            return head.get_value()

        #set the head reference to the current head's next node in the list
        value = self.head.get_value()
        self.head = self.head.get_next()

        return value

    def remove_tail(self):
        # is there a head
        if not self.tail:
            return None
            
         # if head has no next, there is a single element in the linked list 
        if self.head is self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)          
        return value

    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node w're currently at; update this as we travers the linked list
        current = self.head
        # check to see if we're at a valid node
        while current:
            if current.get_value() == value:
                return True
        # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False





