# Implement Node Class

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
    
#     def set_next_node(self, next):
#         self.next = next

#     def get_next_node(self):
#         return self.next

#     def get_value(self):
#         return self.value

# Implement Linked List

# class LinkedList:
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next

    def set_next_node(self, next):
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_tail(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
            self.head.next = self.tail
            return
        # ! point curr tail to newNode
        self.tail.next = node
        self.tail = node
        

    def get_tail(self):
        return self.tail
    
    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next
        return False

    def remove_head(self):
        if not self.head:
            return None
        
        if self.head.next is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value

        head_value = self.head.value
        self.head = self.head.next
        return head_value

    def stringify_list(self):
        string_list = ""
        current_node = self.get_tail()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list


    def remove_tail(self):
        
        """
        remove the tail by deleting the previous nodes reference to it
        prev.next = None
        set the previous node to the tail
        self.tail = prev
        """
        print(self.head.value)
        if self.head == None:
            
            return None
        value = self.tail.value
        prev = node = self.head
        while node.next != None:
            prev = node
            node = node.next
        
        prev.next = None
        self.tail = prev
        return value