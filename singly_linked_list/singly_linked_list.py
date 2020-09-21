# TODO a class that represents that individual elements in our LL

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
    def __init__(self, first_node=None):
        # what attributes do we need?
        self.head = first_node
        self.tail = first_node

    def add_to_head(self, value):
        # create a new Node
        new_node = Node(value)

        if self.head is not None:
            print(f"head: {self.head.value} ", )
        else:
            print(f"head: {self.head} ", )

        if self.tail is not None:
            print(f"tail: {self.tail.value} ")
        else:
            print(f"tail: {self.tail} ")

        print(f"newNode: value: {new_node.value} next: {new_node.next_node} ")

        if self.head is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # set next_node of my new Node to the head
            new_node.set_next_node(self.head)
            # update the head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # create a new Node
        new_node = Node(value)

        # 1. LL is empty
        if self.head is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node
        # 2. LL is NOT empty
        else:
            # update next_node of our tail
            self.tail.set_next_node(new_node)
            # update self, tail
            self.tail = new_node

    def remove_head(self):
        # empty list
        if self.head is None:
            return None
        # else, return VALUE of the old head
        else:
            ret_value = self.head.get_value()
            # list iwth 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # list with +2 elements
            else:
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        # empty lst?
        if self.head is None:
            return None

        # list with 1 element
        ret_value = self.tail.get_value()
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # list with +2 elements
        else:
            cur_node = self.head
            while cur_node.get_next_node() is not self.tail:
                cur_node = cur_node.get_next_node()
            cur_node.set_next_node(None)
            self.tail = cur_node

        return ret_value

    def contains(self, value):
        # loop through LL until next pointer is None
        cur_node = self.head
        while cur_node is not None:
            # if we find 'value'
            if cur_node.get_value() == value:
                print(f"The node contains value {value} ")
                return True
            cur_node = cur_node.next_node
            # return False

    def get_max(self):
        # TODO time permitting
        pass

    def printList(self):
        if self.head is None:
            return "list is empty"
        currentNode = self.head
        ret_value = []
        while True:
            if currentNode is None:
                break
            ret_value.append(currentNode.value)
            currentNode = currentNode.next_node
        return ret_value


# Tests the List
# myList = LinkedList()
# myList.add_to_head(2)
# myList.add_to_head(3)
# myList.add_to_head(4)
# myList.add_to_head(5)


# print(f"myList: {myList.printList()} ")
