class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        curr_node = self.head
        print('-----')
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next
        print('-----')

    def add_to_front(self, value):
        old_head = self.head
        new_head = Node(value)
        new_head.next = old_head
        self.head = new_head


ll = LinkedList()
ll.add_to_front(1)
ll.add_to_front(2)
ll.add_to_front(3)
ll.print()
