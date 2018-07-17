class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.tail == None:  # if tail doesn't exist..probably head doesn't exist also but wise to check explicitly
            if self.head == None:
                self.head = new_node
            else:
                self.tail.next_node = new_node
                self.tail = new_node
    # # Create new node
    #   newNode = Node(value)
    #   # if it is the head is exists, if it does not that means the node added is the only element
    #   if self.head == None:
    #       self.head = newNode
    #       # self.tail = newNode
    #   # if not set the newnode will be directed to tail
    #   else:
    #       self.tail.next_node = newNode
    #       self.tail = newNode

    def remove_head(self):
        if head == None:
            if tail == None:
                return False
                if self.head.next_node != None:
                    head = self.head
                    self.head = self.head.next_node
                    return value

    def contains(self, target):
        if head == None:
            return False
            while(result):
                if result.value == target:
                    return result
                else:
                    result = result.next_node
                    return result

    def get_max(self):
        if self.head == None:
            return False
            maxVal = self.head.value
            current = this.head
            while(current):
                if current.value > maxVal:
                    maxVal = current.value
                    current = current.next
                    return maxVal
