class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        '''add a new node to the tail of the list'''
        # if the list is empty, save to both the head and tail
        if self.head is None:
            newnode = Node(value)
            self.head = newnode
            self.tail = newnode
            self.count += 1
        else:
            # append it onto the tail
            newnode = Node(value)
            self.tail.next = newnode
            self.tail = newnode
            self.count += 1
    
    def contains(self, value):
        # check if there's even a list to search
        if self.head is None:
            return False
        else:
            # start at the head
            curnode = self.head
            # walk down the list checking each value
            while True:
                if value == curnode.value:
                    # found it, return true
                    return True
                
                if curnode.next is None:
                    break

                curnode = curnode.next
            # didn't find it, return false
            return False
    
    def remove_head(self):
        '''return the number removed, like pop()'''
        # check if head is not the only entry in the list
        if self.head is None:
            # if there's nothing, return None
            return None
        elif self.head.next is not None:
            ret = self.head.value
            self.head = self.head.next
            self.count -= 1
            return ret
        else:
            # delete both markers if it is
            ret = self.head.value
            self.head = None
            self.tail = None
            self.count -= 1
            return ret
    
    def get_max(self):
        # check if list exists, return None if it doesn't
        if self.head is None:
            return None
        else:
            curnode = self.head
            maxval = 0
            while True:
                # update value if larger
                if maxval < curnode.value:
                    maxval = curnode.value
                
                if curnode.next is None:
                    break
                # walk through list
                curnode = curnode.next
            # return the largest value
            return maxval

