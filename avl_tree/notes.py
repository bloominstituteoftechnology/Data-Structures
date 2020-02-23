
# linked list stores an array of items. 
# no node accesses previous node, each node can access next node, wrap node in linked list node, always add to tail
# each item in linked list is an object
class ListNode: # box example

    def __init__(self, data=None, next=None):
        self.data = data # what box contains
        self.next = None # refering to the next box ie head.next.next.data refers to the third item in list

    def __repr__(self):
        return repr(self.data)

    # def countNodes(head): # counts number of nodes from head
    #     count = 0
    #     while self.next != None:
    #         count += 1
    #     return self.


class LinkedList: # objects contains node objecsts, can create new nodes, delete nodes, find node
    # adds a node, create a new function
    # 
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        self.head = ListNode(data=data, next=self)

    def append(self, data):
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next: 
            curr = curr.next
        curr.next = ListNode(data=data)
    
    def find(self, key):
        curr = self.head
        while curr and curr.data !=key:
            curr = curr.next
        return curr

    def remove(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

linkedList = LinkedList()
print(linkedList)
linkedList.prepend(23)
linkedList.append('a')
print(linkedList)

# nodeA = Node(6)
# print(nodeA.next)