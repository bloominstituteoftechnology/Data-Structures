class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Function to add a new node to the end of the list:
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current_node = self.head
            # While current_node.next is not none:
            while current_node.next:
                current_node = current_node.next
            # Now that the value of current_node.next is equal to none, we
            # are at the end of the list and we must set the .next value
            # of the current node to the memory address of the new node
            current_node.next = new_node
            # When we traverse to the node that has a next value of none
            # we are at the end of the list and we must now set the prev
            # pointer of the new_node we are adding to the current node
            new_node.prev = current_node
            # Now we set the next value of the new_node to None which
            # signifies that it is the new tail on the list
            new_node.next = None

    # Function to add a new_node to the front of the doubly linked list
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    # Function to delete a node from a doubly linked list:
    def delete_node(self, key):
        current_node = self.head
        # While current_node is not None:
        while current_node:
            if current_node.data == key and current_node == self.head:
                # If the next value of the current node is None, this means
                # that the current node is the ONLY node in the list
                if not current_node.next:
                    current_node = None
                    self.head = None
                    return
                else:
                    # next is equal to the next pointer of current_node.next
                    next = current_node.next
                    # Remove the next pointer from the current_node
                    current_node.next = None
                    # The previous pointer of the next element in the list now
                    # points to none signifying it is now the first element in
                    # the list
                    next.previous = None
                    # Remove/Delete the current_node from the list
                    current_node = None
                    # Update the self.head node to the next node in the list to
                    # the node that is next in the sequence
                    self.head = next
                    return
            elif current_node.data == key:
                # if current_node.next has a node after it:
                if current_node.next:
                    next = current_node.next
                    prev = current_node.prev
                    prev.next = next
                    next.prev = prev
                    current_node.next = None
                    current_node.prev = None
                    current_node = None
                    return
                else:
                    prev = current_node.prev
                    prev.next = None
                    current_node.prev = None
                    current_node = None
                    return
            current_node = current_node.next

    # Function to display the elements in the list

    def display_list(self):
        current_node = self.head
        # While the value of current node is not None
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # Function to add_after_node:

    def add_after_node(self, key, data):
        current_node = self.head
        while current_node:
            if current_node.next is None and current_node.data == key:
                self.append(data)
                return
            elif current_node.data == key:
                new_node = Node(data)
                next = current_node.next
                current_node.next = new_node
                new_node.next = next
                new_node.prev = current_node
                next.prev = new_node
            current_node = current_node.next

            # Function to add before a given node:

    def add_before_node(self, key, data):
        pass


double_linked_list = DoublyLinkedList()

double_linked_list.display_list()

double_linked_list.prepend("A")
double_linked_list.append(0)
double_linked_list.append(1)
double_linked_list.append(2)
double_linked_list.append(3)
double_linked_list.append(4)
double_linked_list.prepend(
    "Prepend Working for Double Linked Lists Having More Than One Node")

double_linked_list.display_list()

double_linked_list.add_after_node(1, 11)

double_linked_list.delete_node("A")

double_linked_list.display_list()
