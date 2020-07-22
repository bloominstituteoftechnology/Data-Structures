class Node:
    def __init__(self, value= None, next_node = None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_head(self,value):
        #create a node for the value
        new_node = Node(value)
        #check if list is empty
        if self.head is None and self.tail is None:
            #store the new node that correspond to both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            #new node should point to the current head
            new_node.next_node = self.head
            # move head to the next node
            self.head = new_node    

    def add_to_tail(self, value):
        #create a node for the value
        new_node= Node(value)
        #Check if list is empty
        if self.head is None and self.tail is None:
            #store the new node that correspond to the both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            #node at current tail point to the new node
            self.tail.next_node = new_node
            # tail will point to the new node
            self.tail = new_node
    def remove_head(self):
       #if list is empty return none
       if not self.head:
           return None 
       #if list has only one element
       if self.head.next_node is None:
           head_value = self.head.value
           self.head = None
           self.tail = None
           return head_value
       else:
           head_value = self.head.value
           # head will point the node next to the current node
           self.head = self.head.next_node 
           return head_value
    def contains(self, value):
        if self.head is None:
            return None
        # create node for the value
        current_node = self.head
        # loop through each node until we see the value or we can't go further
        while current_node !=None:
            if current_node.value ==value:
                return True
            #othewise go to the next node
            current_node= current_node.next_node
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






