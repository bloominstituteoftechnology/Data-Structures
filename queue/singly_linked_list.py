class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setNext(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __len__(self):
        return self.length

    def getLength(self):
        if self.length == 0:
            return 0
        else:
            return self.length

    def __str__(self):
        if self.length == 0:
            return 'The Linked List is Empty!'
        n = self.head
        output = ''
        output += f'({n.value})->'
        while n is not None:
            output += f'({n.value})->'
            n = n.next
        return output

    def add_to_head(self, value):
        new_node = Node(value)
        self.head = new_node

        if self.length == 0: # if self.head is None and self.tail is None:
            self.tail = new_node

        self.length += 1

    def remove_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.getValue()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.getValue()
            self.head = self.head.getNext()
            self.length -= 1
            return value


    def add_to_tail(self, value):
        new_node = Node(value)

        if self.length == 0: # if self.tail is None and self.head is None:
            self.head = new_node
        else:
            self.tail.setNext(new_node)

        self.tail = new_node
        self.length += 1


    def remove_tail(self):
        if self.tail is None:
            return None
        elif self.tail == self.head:
            value = self.tail.getValue()
            self.tail = None
            self.head = None
            self.length -=1
            return value
        else:
            value = self.tail.getValue()
            current_node = self.head
            while current_node.getNext() is not self.tail:
                current_node = current_node.getNext()
            current_node.setNext(None)
            self.tail = current_node
            self.length -=1
            return value



    def contains(self, value):
        if self.head is None:
            return False
        else:
            l = 0
            n = self.head
            while l is not self.length:
                print(f'\nn = {n.value}, l = {l}, and Length = {self.length}')
                if n.value == value:
                    return True
                else:
                    l += 1 
                    n = n.next
            return False

    def get_max(self):
        if self.length == 0:
            print('max is None')
            return None
        elif self.length == 1:
            return self.head.value
        else:
            n = self.head
            j = n.next
            max = self.head.value
            while n.next is not None:
                print(f'j = {j.value}')
                if j.value > n.value:
                    max = j.value
                elif n.value > j.value:
                    max = n.value
                
                n = n.next
                j = n.next
            print(f'max is {max}')
            return max

