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
        print(f'Adding new node to tail: {node.value}')

    def remove_head(self):
        # if self.head == None:
        #     return None
        # # set the head nodes next node value to a temp var

        # old_head = self.head.value
        # self.head = self.head.get_next()
        # # delete the head node
        # # del(self.head)
        # # then set head to that temp

        # # print(
        # #     f'Removing node from head: {old_head}, new head is {new_head.value}')
        # print(f' this is the old head {old_head}')
        # return old_head
        if self.head == None:
            return self.head
        # set the head nodes next node value to a temp var
        else:
            old_head = self.head.value
            self.head = self.head.get_next()
            # handle a case where head is the one and only node in linked list
            if self.head is None:
                self.tail = None
            print(f' this is the old head {old_head}')
            return old_head

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

        if current_node == None:
            cur_max = None

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
myList.add_to_tail(2939)
myList.remove_head()
myList.remove_head()
myList.remove_head()

print(myList.get_max())
print(myList.contains(2939))
