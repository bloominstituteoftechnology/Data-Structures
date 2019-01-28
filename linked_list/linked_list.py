"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""


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
        # create new node
        node = Node(value)
        # if the LL is not empty
        if self.tail is not None:
            self.tail.set_next(node)
        else:
            # if it is empty, set the new node to the head
            self.head = node
        # set the LL's tail to the new node
        self.tail = node

    def remove_head(self):
        # set the head nodes next node value to a temp var
        new_head = self.head.next_node
        # delete the head node
        del(self.head)
        # then set head to that temp
        self.head = new_head

    def contains(self, value):
        # starts at head
        # loop WHILE cur_node.next_node != NULL
        # if cur_node.value == value, return True
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.get_next()
        return False
        # after loop exits if not found, return False

    def get_max(self):
        current_node = self.head
        cur_max = 0

        while current_node is not None:
            if current_node.value > cur_max:
                cur_max = current_node.value
            current_node = current_node.get_next()
        return cur_max

        # cur_max, biggest value so far
        # for each value: compare value to cur_max
        # if Node.value  > cur_max, update cur_max

        # return cur_max


myList = LinkedList()
myList.add_to_tail(6)
myList.add_to_tail(3)
myList.add_to_tail(10)
myList.get_max()

print(myList.contains(10))
