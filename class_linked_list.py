class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        # The current node we are looking at:
        current_node = self.head
        # Iterate over the entire LinkedList until the value at self.next
        # is equal to None...then add the new_node to the end of the list
        while current_node.next is not None:
            current_node = current_node.next
        # When we know that we are at the end of the list we will now
        # append new_node to the end of the list
        current_node.next = new_node

    def length(self):
        current_node = self.head
        total = 0
        # Iterate over the nodes in the list and increment the
        # counter variable for each new_node where the self.next
        # value is not equal to none
        while current_node.next is not None:
            total = total + 1
            # Traverse through to the next node
            current_node = current_node.next
        return total

    def display_list(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    # Function to pull out the element at a specific index:
    def get_element(self, index):
        # Make sure that the index passed into the function
        # is not outside of the range of our List
        if index >= self.length():
            print("get_element index out of range")
            return None
        current_index = 0
        current_node = self.head
        # We do not need to worry that this is an infinite loop because we
        # already check to see if the index provided was in range for the
        # loop in the above statement
        while True:
            current_node = current_node.next
            # If the current node index is equal to the index provided
            # by the user, then return the data stored at that node to the user
            if current_index == index:
                return current_node.data
            # Otherwise, continue to traverse from node to node while
            # incrementing the current_index
            current_index = current_index + 1

    # Function to erase/remove a node at a specified index:
    def erase_element(self, index):
        if index >= self.length():
            print("erase_element index provided is out of range")
            return
        current_index = 0
        current_node = self.head
        while True:
            # We need to save the node prior to the one that we want to erase
            # to make sure that it then points to the node next to the one that
            # we just erased
            previous_node = current_node
            current_node = current_node.next
            if current_index == index:
                # We don't have to erase the node, all we have to do is point
                # the previous node to the memory address of the
                # next_node value for the node we want to erase
                previous_node.next = current_node.next
                return
            current_index = current_index + 1


my_list = LinkedList()

my_list.display_list()

my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display_list()

my_list.erase_element(1)

my_list.display_list()
