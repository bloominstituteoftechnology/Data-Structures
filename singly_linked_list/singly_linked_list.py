

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next    # The next node in the list


class LinkedList:
    def __init__(self):
        self.head = None    # Points to the first node in the list
        self.tail = None    # Points to the last node in the list
        self.length = 0

    # append / add --> add_to_tail
    def add_to_tail(self, value):
        if not self.tail:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail

        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
        self.length += 1

    # remove
    def remove_head(self):
        if not self.head:
            return None

        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value

        else:
            current_head = self.head
            self.head = current_head.next
            self.length -= 1
            return current_head.value

    def remove_tail(self):
        # Remove Tail:
        if self.tail is None:
            return None
        # List of 1 element:
        if self.head == self.tail:
            # Save the current_tail.value
            current_tail = self.tail
            # Set self.tail to None
            self.tail = None
            # Set self.head to None
            self.head = None
            self.length = self.length - 1
            return current_tail.value
        # Check if it's there
        # General case:
        else:
            # Start at head and iterate to the next-to-last node
            current_node = self.head
            # Stop when current_node.next == self.tail
            while current_node.next != self.tail:
                current_node = current_node.next
            # Once we exit the while loop, current_node is pointing to the node right before self.tail
            # Save the current_tail value
            current_tail = self.tail
            # Set self.tail to current_node
            self.tail = current_node
            # Set current_node.next to None
            current_node.next = None
            self.length = self.length - 1
            return current_tail.value

    def add_to_head(self, value):
        if self.head is None:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            new_node = Node(value, self.head)
            self.head = new_node
            self.length += 1

    def remove_at_index(self, value):
        pass
