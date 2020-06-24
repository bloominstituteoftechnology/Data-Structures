class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.head = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
    
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


linked_list = LinkedList()

linked_list.add_to_tail(1)
print(linked_list.head.value)
print(linked_list.tail.value)




