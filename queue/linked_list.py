class Node:
    def __init__(self, value= None, next_node= None):
        self.value = value
        self.next_node = next_node

# manager of the nodes
class LinkedList:
    def __init__(self):
        self.head = None # Stores a node, the first node in list
        self.tail = None # Stores a node that is at the end of the list
    
    # return all values in the list a --> b --> c --> d --> None
    def __str__(self):
        output = ''

        # will always need the 4 commented lines below to loop through linked lists
        current_node = self.head # create a tracker node variable
        while current_node is not None: # loop until it's None
            output += f'{current_node.value} --> ' # working on current node
            current_node = current_node.next_node  # update the tracker to next node
        return output

    # add to head
    def add_to_head(self, value):
        # create node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    # add to tail
    def add_to_tail(self, value):
        # create node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point node at current tail to the new node
            self.tail.next_node = new_node
            # move tail to new node
            self.tail = new_node

    # remove value from head and return the value
    def remove_head(self):
        # if list is empty, return nothing, no deletion
        if not self.head:
            return None
        # if list has only one element, set head/tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # if there are more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value


    # figure out if certain elements are in a list
    def contains(self, value):
        # if list is empty
        if not self.head:
            return False
        # loop through nodes to find our node until we reach the tail
        current_node = self.head
        # 
        while current_node is not None:
            # is this the node we are looking for?
            if current_node.value == value:
                return True
            # otherwise move to next node
            current_node = current_node.next_node
        return False

# try it all out

linked_list = LinkedList()
# add 0 to the list
linked_list.add_to_head(0)
# add 1 to the tail
linked_list.add_to_tail(1)

# list checks
print(f'Does the Linked List contain 0? {linked_list.contains(0)}')
print(f'Does the Linked List contain 1? {linked_list.contains(1)}')
# check to make sure we can get a false
print(f'Does the Linked List contain 3? {linked_list.contains(3)}')

# add 2, then 5 to front
linked_list.add_to_head(2)
print(f'The start of the list is: {linked_list.head.value}')
linked_list.add_to_head(5)
print(f'The start of the list is: {linked_list.head.value}')
# check that remove works
linked_list.remove_head()
print(f'The start of the list is: {linked_list.head.value}')
print(linked_list)