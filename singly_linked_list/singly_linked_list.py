#A linked list is a sequence of data items, just like an array. But where an array allocates a big block of memory to store the objects, the elements in a linked list are totally separate objects in memory and are connected through links:
#create Node

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return self.value

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if not self.tail:
            self.tail = new_node
    
    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        
        removed_value = self.head.get_value()
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed_value

    def remove_tail(self):
        if not self.head:
            return None
        
        curr = self.head
        prev = curr
        while curr.get_next() != None:
            prev = curr
            curr = curr.get_next()
        
        prev.set_next(None)
        self.tail = prev
        return curr
    
    def get_max(self):
        if not self.head:
            return None
        
        curr = self.head
        max_value = curr.get_value()
        while curr != None:
            max_value = max(max_value, curr.get_value())
            curr = curr.get_next()
        return max_value
    
    def contains(self, value):
        curr = self.head
        while curr != None:
            if curr.get_value() is value:
                return True
            curr = curr.get_next()
        return False

linked_list = LinkedList()
linked_list.add_to_head(0)
linked_list.add_to_tail(1)
print(f'Does our linked list contains 0: {linked_list.contains(0)}')
print(f'Does our linked list contains 1: {linked_list.contains(1)}')
print(f'Does our linked list contains 2: {linked_list.contains(2)}')
linked_list.add_to_head(2)
print(f'start of the list: {linked_list.head.value}')
linked_list.add_to_head(5)
print(f'start of the list: {linked_list.head.value}')
linked_list.remove_head()
print(f'start of the list: {linked_list.head.value}')
