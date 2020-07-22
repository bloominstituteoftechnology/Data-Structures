
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
    def __init__(self, head, tail):
        self.head = head_node
        self.tail = tail_node

    def add_to_head():
        pass

    def remove_head():
        pass

    def add_to_tail():
        pass

    def remove_tail():
        pass
