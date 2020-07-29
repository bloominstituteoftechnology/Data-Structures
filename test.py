#middle node: How do you find and return the middle node of a singly linked list in one pass? You do not have access to the length of the list. If the list is even, you should return the first of the two "middle" nodes. You may not store the nodes in another data structure.

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = next

    def add(self, value):
        self.next = Node(value)

    def find_middle(self):
        middle = self
        end = self 
        while end != None:
            end = end.next
            if end:
                end = end.next
                middle = middle.next
            print("Middle is" + str(middle.value))

root = Node(1)
cur = root
cur.add(2)
cur = cur.next
cur.add(3)

cur = cur.next
cur=root

cur.find_middle()