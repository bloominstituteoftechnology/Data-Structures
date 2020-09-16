class Node: 
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_text): 
        self.next = new_text


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self,value):
        new_node = Node(value)

        if self.tail is None and self.tail is None: 
            # in a one-element linked list, what should head and tail be referring to?
            # have both head and tail reffering to the single node.
            self.head = new_node
            # set the new node to be the tail.
            self.tail = new_node

        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None and self.tail is None:
            return

        if not self.head.get_next():
            head = self.head
            self.head = head
            self.tail = None
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    # def remove_head(self):
    #     if self.head is None and self.tail is None:
    #         return
    #     if not self.head.get_next():
    #         head = self.head
    #         self.head = None
    #         self.tail = None
    #         return head.get_value()

    #     value = self.head.get_value()
    #     self.head = self.head.get_next()
    #     return value

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return 

        if self.head == self.tail:
            # store the node so we can remove the value
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        else: 
            val = self.tail.get_value()
            current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()


        self.tail = current
        self.tail.set_next(None)
        self.tail = current
        return val