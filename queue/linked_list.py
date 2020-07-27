class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # def __str__(self):
    #     output = " "
    #     current_node = self.head
    #     while current_node is not None:
    #         output += f"{current_node} --> "
    #         current_node = current_node.next_node
    #     return current_node


    def add_to_head(self, value):
        new_node = Node(value)
        # if the list is empty
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        # if there is an item in the list
        else:
            new_node.next_node = self.head
            self.head = new_node 

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        # if there is an element on the list
        else:
            self.tail.next_node = new_node
            self.tail = new_node 

    def remove_head(self):
        # if there the list is empty
        if self.head == None and self.tail == None:
            return None
        # if the list only contains one item
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # if there is more than one item in the list
        head_value = self.head.value
        self.head = self.head.next_node

        return head_value


    def remove_tail(self):
        # if empty
        if self.head == None and self.tail == None:
            return 
        # if there is only one item
        if self.head.next_node == None:
            current_value = self.head.value
            self.head = None
            self.tail = None
            return current_value
        # if there is more than one item
        tail_value = self.tail.value
        self.tail = self.tail.next_node

        return tail.value

