# singly_linked_list/singly_linked_list.py

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        output = ""
        current_node = self.head
        while current_node is not None:
            output += f"{current_node.value} -->"
            current_node = current_node.get_next()

        return output
        

    def add_to_tail(self, value):
        # 1. create the Node from the value 
        new_node = Node(value)
        # So, what do we do if tail is None? 
        # What's the rule we want to set to indicate that the linked
        # list is empty? 
        # Would it be better to check the head? 
        # Let's check them both: an empty linked list has an empty 
        # head and an empty tail 
        if self.head is None and self.tail is None:
            # in a one-element linked list, what should head and tail 
            # be referring to? 
            # have both head and tail referring to the single node 
            self.head = new_node
            # set the new node to be the tail 
            self.tail = new_node
        else:
            # These steps assume that the tail is already referring
            # to a Node 
            # 2. set the old tail's next to refer to the new Node 
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node 
            self.tail = new_node

    def remove_head(self):
        # if we have an empty linked list 
        if self.head is None and self.tail is None:
            return
        # what if we only have a single elem in the linked list?
        # both head and tail are pointing at the same Node 
        if not self.head.get_next():
            head = self.head 
            # delete the linked list's head reference 
            self.head = None
            # also delete the linked list's tail reference 
            self.tail = None 
            return head.get_value()
        val = self.head.get_value()
        # set self.head to the Node after the head 
        self.head = self.head.get_next()
        return val

    def remove_tail(self):
        # if we have an empty linked list 
        if self.head is None and self.tail is None:
            return

        # handle a single-element linked list
        elif self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
		
        # if we have a non-empty linked list 
        # we have to start at the head and move down the linked list 
        # until we get to the node right before the tail 
        # iterate over our linked list 
        current = self.head

        while current.get_next() and current.get_next() is not self.tail:
            current = current.get_next()

        # at this point, `current` is the node right before the tail 
        # set the tail to be None
        value = self.tail.get_value()
        self.tail = current
        # remove new tail's reference to the old tail
        self.tail.set_next(None)
        return value
            

    def contains(self, value):
        if not self.head:
            return False
    
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value


if __name__ == "__main__":
    ll = LinkedList()

    for i in range(1, 6):
        ll.add_to_tail(Node(2**i))

    print(ll)
