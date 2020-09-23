# A class that represents the individual elements in our LL

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            # update head attribute
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def remove_head(self):
        # empty list
        if self.head is None:
            return None

        # list with one node
        else:
            ret_value = self.head.get_value()

            if self.head == self.tail:
                self.head = None
                self.tail = None

        # list with two nodes +
            else:
                self.head = self.head.get_next_node()

            return ret_value

    def remove_tail(self):

        if self.tail is None:
            return None

        else:
            ret_value = self.tail.get_value()
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current_node = self.head
                while current_node is not None:
                    if current_node.get_next_node() == self.tail:
                        break

                    current_node = current_node.get_next_node()

                self.tail = current_node
                self.tail.set_next_node(None)

            print("outside value", ret_value)
            return ret_value

    def contains(self, value):
        # Loop through LL until next pointer is none
        # if equal, break and return true
        current_node = self.head
        while current_node is not None:
            if current_node.get_value == value:
                return True
        return False

    def get_max(self):
        # loop and store highest value
        highest = 0
        current_node = self.head

        while current_node is not None:
            if current_node.value > highest:
                highest = current_node.value
            current_node = current_node.next_node
        return highest
