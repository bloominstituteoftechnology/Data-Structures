class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = Node(value)

    def add_to_tail(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.tail)
        self.tail = new_node

    def get_tail(self):
        return self.tail
    
    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next_node
        return False

    def remove_head(self):
        if not self.head:
            return None
        
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value

        head_value = self.head.next_node
        self.head = self.head.next_node
        return head_value

    def stringify_list(self):
        string_list = ""
        current_node = self.get_tail()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

ll = LinkedList()


ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(5)
ll.add_to_tail(10)


print(ll.stringify_list())


