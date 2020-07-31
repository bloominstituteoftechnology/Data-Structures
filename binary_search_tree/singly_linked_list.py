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
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:    # if self.head is None and self.tail is None:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        # empty LL
        if self.head is None:
            return None

        # LL with 1 Node
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        # LL with 2+ Nodes
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        # empty LL
        if self.head is None:
            return None

        # LL with 1 Node
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        # LL with 2+ Nodes
        else:
            current = self.head
            while current.get_next() is not self.tail:
                current = current.get_next()
            value = self.tail.get_value()
            current.set_next(None)
            self.tail = current
            self.length -= 1
            return value
            
    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        if self.head is None:
            return None
        # iterate through all the elements
        cur_node = self.head
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()
        return cur_max

    # interview question to find the middle value by only going through list one time
    def find_middle(self):
        # doing this in 1 pass, without using `length` attribute
        mid_point = self.head
        end_point = self.head
        while end_point is not None and end_point.get_next() is not None:
            mid_point = mid_point.get_next()
            end_point = end_point.get_next().get_next()

        return mid_point.value

    # interview question: How do you reverse a singly linked list without recursion? You may not store the list, or it's values, in another data structure.
    def reverse_ll(self):
        cur_node = self.head
        next_node = cur_node.next
        # head points to None
        cur_node.set_next(None)
        self.tail = cur_node
        while next_node is not None:
            prev_node = cur_node
            cur_node = next_node
            next_node = cur_node.get_next()
            cur_node.set_next(prev_node)
        self.head = cur_node


ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)
ll.add_to_tail(5)
ll.add_to_tail(6)
ll.add_to_tail(7)
ll.add_to_tail(8)
ll.add_to_tail(9)
print(ll.find_middle())