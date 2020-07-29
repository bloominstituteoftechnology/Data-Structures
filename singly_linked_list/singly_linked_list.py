class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next
    def set_next(self,new_node):
        self.next=new_node

class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
    def add_to_tail(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.set_next(new_node)
            self.tail=new_node
    def remove_head(self):
        if not self.head:
            return None
        if not self.head.get_next():
            head=self.head
            self.head=None
            self.tail=None
            return head.get_value()
        value=self.head.get_value()
        self.head=self.head.get_next()
        return value
    def remove_tail(self):
        if not self.head:
            return None
        elif self.head.get_next()==None:
            head=self.head.get_value()
            self.head=None
            self.tail=None
            return head
        node1=self.head
        node2=self.head.get_next()
        while node2.get_next() != None:
            node1=node2
            node2=node2.get_next()
        node1.set_next(None)
        return node2.get_value()
            

    def contains(self,value):
        if not self.head:
            return False
        current=self.head
        while current:
            if current.get_value()==value:
                return True
            current=current.get_next()
        return False
    def get_max(self):
        max_value=0
        if not self.head:
            return None
        current=self.head  
        while current:
            if (max_value < current.get_value()):
                max_value=current.get_value()
            current=current.get_next()
        return max_value
    def length(self):
        count=0
        current=self.head
        while self.head != None:
            count+=1
            current=self.head.get_next()
        return count
    
        
            

        
        

        
