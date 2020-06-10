class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def get_data(self):
        # returns the node's data
        return self.data
    
    def get_next(self):
        # returns the thing pointed at by this node's `next` reference
        return self.next
    
    def set_next(self, new_next):
        # sets this node's `next` reference to `new_next`
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, data):
        # adds `data` to the end of LinkedList
        # wrap the `data` in a Node to instance
        new_node = Node(data)

        # what about empty case, where both self.head = None and self.tail = None
        if not self.head and not self.tail:
            # list is empty
            # update both head and tail to point to the new node
            self.head = new_node
            self.tail = new_node
        # non-empty linked list case
        else:
            # call set_next with the new_node on the current tail node
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_from_head(self):
        # removes the Node that `self.head` is referring to and returns the Node's data
        if self.head is None:
            return None

        data = self.head.get_data()
        # both head and tail refer to the same Node
        # there's only one Node in the linked list
        if self.head is self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else: 
            # save the head Node's data
            # delete the head Node 
            # update `self.head` to refer to the Node after the Node we just deleted 
            self.head = self.head.get_next()

        
        return data


        
'''

node = Node(1)
node.set_next(Node(2))
node.get_next().set_next(Node(3))
node.get_next().get_next().set_next(Node(4))

'''