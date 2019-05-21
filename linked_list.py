class Node:
    def __init__(self, value=None, next_node=None):
        # the value of this node
        self.value = value
        # a pointer to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next pointer to be the passed in node
        self.next_node = new_next
        # string representation of our Node class in the console

    def __repr__(self):
        return f'{self.value}'


# our linked list will be composed of Nodes


class LinkedList:
    def __init__(self):
        # the linked list stores two properties
        # one for the head and one for the tail
        self.head = None
        self.tail = None

    # O(1)
    def add_to_tail(self, value):
        # wrap the input value in a node
        new_node = Node(value, None)
        # check if the list is empty
        if not self.head:
            # if it is, set this new node to be head
            self.head = new_node
            self.tail = new_node
        # set the next_node property on the old tail to be the new one
        # if not empty, set the new node to be the tail
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    # removes the head element
    # returns the value of the removed head
    # O(1)
    def remove_head(self):
        # remove the head
        # check if head is none:
        if self.head != None:
            # Store next node into a variable
            new_head = self.head.next_node
            # Store a return value
            result = self.head
            # Delete the old head
            del(self.head)
            # set head to next node
            self.head = new_head
            return result

    # find if a value exists in our list
    # returns a boolean
    # O(1) best case
    # O(n) worst case
    def contains(self, value):
        # check if the list is empty
        if not self.head:
            return False
        # check if the value is the head or tail
        if self.head.get_value() == value or self.tail.get_value() == value:
            return True
        # get a reference to the node we're currently at
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if current.get_value is equal to the passed in value
            if current.get_value() == value:
                return True
            # otherwise change current to be the next node and keep searching
            current = current.get_next()
        # if we get here the while loop didn't find the value
        # so, return false
        return False


my_list = LinkedList()
print("Head:", my_list.head)
print("Tail:",my_list.tail)
print("adding to empty list")
my_list.add_to_tail(3)
print(my_list.head)
print(my_list.tail)
print("adding 6")
my_list.add_to_tail(6)
print(my_list.head)
print(my_list.tail)
print("adding 4")
my_list.add_to_tail(4)
print(my_list.head)
print(my_list.tail)
print("searching for 4")
print(my_list.contains(4))
print("searching for 5")
print(my_list.contains(5))
print("removing 3")
print(my_list.remove_head())
print(my_list.head)
print(my_list.tail)
print("removing 6")
print(my_list.remove_head())
print(my_list.head)
print(my_list.tail)
"""
class Node:
    def __init__(self, value=None, next_node=None):
        # the value of this node
        self.value = value
        # a pointer to the next node in the list
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
    
    # string representation of our node dclase
    def __repr__(self):
        return f'String {self.value}'

# our linked list will be composed of Nodes
class LinkedList:
    def __init__(self, head = None):
        # the linked list stores two properties
        # one for the head and one for the tail
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap input value in a node
        new_node = Node(value) #new_node = Node(value, None)
        # check if the list is empty
        if not self.head:
        # if  it is, set the new node to be hte head
            self.head = new_node
            self.tail = new_node
        # if not empty, set the new node to be the tail
        # set the next_node property on the old tail to be the new one
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        # remove head
        # set head.next_node to be our new head
        value = self.head.get_value()
        #check if our head has a next_node
        if not self.head.get_next():
            # store the current head in a variable
            self.head = None
            self.tail = None
            #return the value of the old head
            return value
        
        # if our list has more than one element
        # set the head to be the next item in the list
        self.head = self.head.get_next()
        # return the value of the old head
        return value
    
    # find if a value exists is our list
    # returns a boolean
    def contains(self, value):
        # check if the list is empty
        if not self.head:
            return False
        # check if the value is the head or tail
        if self.head.get_value() == value or self.tail == value:
            return True
        # get a reference to the node we're currently at
        current = self.head
        # check to se if we're at a valid node
        while current:
            # return True if current.get_value is equal to the passed in value
            if current.get_value() == value:
                return True
            # otherwise change current to be the next node and keep searching
            current = current.get_next()
        # if we get here the while loop didn't find the value
        # so, return false
        return False

my_list = LinkedList()
print("adding to empty list")
my_list.add_to_tail(3)
print(my_list.head)
print(my_list.tail)
my_list.add_to_tail(4)
print(my_list.head)
print(my_list.tail)
my_list.add_to_tail(6)
print(my_list.head)
print(my_list.tail)
print(my_list.contains(4))
print(my_list.contains(5))
"""