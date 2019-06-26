class Queue:
    def __init__(self):
        self.size = 0
        self.storage = SingleLinkedList()

    def enqueue(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
        self.storage.add_list_item(item)
        self.size += 1
        
    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.rem_first_item()

    def len(self):
        return self.size

class ListNode:
    def __init__(self,data):
        self.data = data
        
        self.next = None
        return
    
    def has_value(self,value):
        if self.data == value:
            return True
        else:
            return False
            
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        return
    
    def add_list_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
            
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
            
        self.tail = item
        self.length += 1
        return
    
    def rem_first_item(self):
        current_node = self.head
        
        if current_node is not None:
            self.head = current_node.next
            current_node.next = None
            self.length -= 1
        return current_node.data




