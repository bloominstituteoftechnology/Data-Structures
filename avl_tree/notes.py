
# linked list stores an array of items. 
# no node accesses previous node, each node can access next node, wrap node in linked list node, always add to tail
# each item in linked list is an object
class Node: # box example

    def __init__(self, data):
        self.data = data # what box contains
        self.next = next # refering to the next box ie head.next.next.data refers to the third item in list
        self.box = data

nodeA 

class LinkedList: # objects contains node objecsts, can create new nodes, delete nodes, find node
