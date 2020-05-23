class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
    
    def add_to_tail(self, value):
        new_Node = ListNode(value, None)
        # There is a tail
        if self.tail:
            self.tail.next = new_Node
        # There is no tail
        else:
            self.head = new_Node
        
        self.tail = new_Node

    def contains(self, content):
        if not self.head:
            print("Nothing to see here")
            return False
        
        else:
            checkingnode = self.head

            while checkingnode is not None:
                if checkingnode.value == content:
                    return True

                else:
                    pass
                checkingnode = checkingnode.next

            return False
    
    def remove_head(self):
        # empty list
        if not self.head:
            print("Nothing to see here")
        
        # List with one node
        elif self.head == self.tail:
            delvalue = self.head.value
            self.head = None
            self.tail = None
            return delvalue 

        # List with more that one node
        else:
            delvalue = self.head.value
            next_head = self.head.next
            self.head = next_head
            return delvalue

    def remove_tail(self):
        # empty list
        if not self.head:
            print("Nothing to see here")
            return None
        
        # List with one node
        elif self.head == self.tail:
            delvalue = self.head.value
            self.head = None
            self.tail = None
            return delvalue 

        # List with more that one node
        else:
            checknode = self.head
            while checknode.next != self.tail:
                checknode = checknode.next
            
            delvalue = self.tail.value
            self.tail = checknode
            return delvalue
    
    def get_max(self):
        # empty list
        if not self.head:
            print("Nothing to see here")
        # List with at least one node
        else:
            checkingnode = self.head
            maxvalue = self.head.value
            while checkingnode is not None:
                if checkingnode.value > maxvalue:
                    maxvalue = checkingnode.value

                checkingnode = checkingnode.next
            
            return maxvalue
            