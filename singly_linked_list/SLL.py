
class Node:
    def __init__(self, data=None):
        self.data = data
        # Where the pointer to the next node will be stored
        self.next = None # The last element's next pointer will always be None

class LinkedList:
    def __init__(self):
        # Placeholder to allow us to point to the first element in the list
        self.head = Node()

    def append(self, data):
        # This is the first element of the SLL
        new_node = Node(data)
        cur = self.head

        while cur.next != None:
            cur = cur.next
        cur.next = new_node