
class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.lenth += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        # Empty Linked List
        if self.head is None:
            return None
        # List with 1 node
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # List with 2+ nodes
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value
            
    def remove_tail(self):
        # Empty LL
        if self.tail is None:
            return None
        # LL with one value
        elif self.tail == self.head:
            value = self.tail.get_value()
            self.tail = None
            self.head = None
            self.length -= 1
            return value
        # LL with 2 or more
        else:
            cur_node = self.head
            while cur_node.get_next() is not self.tail:
                cur_node = cur_node.get_next()
            value = self.tail.get_value()
            cur_node.set_next(None)
            self.tail = cur_node
            self.length -= 1
            return value

    def contains(self, value):
        current = self.head
        found = False
        while current and not found:
            if current.value == value:
                found = True
            else:
                current = current.get_next()
        if not current:
            return False
        return True        

    def get_max(self):
        if self.head is None:
            return None
        # Iterate through all the elements
        cur_node = self.head 
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()

        return cur_max

    def find_middle(self):
        # Doing this in 1 pass without 'length' attribute
        mid_point = self.head
        end_point = self.head
        while end_point is not None and end_point.get_next() is not None:
            mid_point = mid_point.get_next()
            end_point = end_point.get_next().get_next()
        
        return mid_point.value