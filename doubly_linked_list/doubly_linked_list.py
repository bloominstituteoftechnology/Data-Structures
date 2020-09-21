"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # instantiate a new node
        new_node = ListNode(value)
        #if self.head is None
        if self.head is None and self.tail is None:
            # set head's previous to None
            new_node.prev = None
            # set new node as head
            self.head = new_node 
            self.tail = new_node
            # update length
            self.length += 1
        # if self.head is not None
        else:
            # set new_node as current head's previous node 
            self.head.prev = new_node
            # set current head as next for new_node
            new_node.next = self.head
            # set new new_node as new head
            self.head = new_node
            # set new head's previous as None
            new_node.prev = None
            # update tail
            curr = self.head
            while curr.next:
                curr = curr.next
            self.tail = curr
            # update length
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # if there is no head, then list is emply (nothing to remove)
        if self.head is None:
            # return None
            return None
        # if there is a head but there in no next node
        if self.head and self.head.next is None:
            # store the current head value of the node that we are going to remove
            current = self.head.value
            # remove the node
            # set head and the tail to None
            self.head = None
            self.tail = None
            # update length of the list
            self.length -= 1
            # return the stored value
            return current
        # otherwise (when head is present and next is present)
        else:
            # get the value of the current head
            current = self.head.value
            # set next node as a new head
            self.head = self.head.next
            # set head's previous as None
            self.head.prev = None 
            # update tail
            curr = self.head
            while curr.next:
                curr = curr.next
            self.tail = curr
            # update length
            self.length -= 1
            # return the removed node's value 
            return current
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # instantiate a new node
        new_node = ListNode(value)
        # if there is no head and no tail
        if self.head is None and self.tail is None:
            # assign new node to head and tail
            self.head = new_node
            self.tail = new_node
            # update length
            self.length += 1
        # otherwise
        else:
            # set the new_node as the current tail's next
            self.tail.next = new_node
            # set the current tail as previous node of the new node
            new_node.prev = self.tail
            # set the new node as a new tail
            self.tail = new_node
            # update length
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # if there is no tail and no head
        if self.tail is None and self.head is None:
            # return None
            return None
        # if there is only one node in a list 
        if self.tail and self.tail.prev is None:
            # store the current tail's value
            current = self.tail.value
            # set head and tail to None
            self.head = None
            self.tail = None
            # update length
            self.length -= 1
        # otherwise (if there is previous node of the tail)
        else:
            # store current tail's value
            current = self.tail.value
            # set current tail's previous node as a new tail  
            self.tail = self.tail.prev
            # set new tail's next value as None
            self.tail.next = None
            # update length
            self.length -= 1
        # return removed tail's value
        return current    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # check if the node passed is a tail of the list
        if node == self.tail:
            # set prev tail's value as a new tail 
            self.tail = self.tail.prev
            # set new tail's next value to None
            self.tail.next = None
        # set old tail's node as a prev of current head
        self.head.prev = node
        # set current head as a next node of this node
        node.next = self.head
        # set this node as a new head 
        self.head = node
        # set head prev to None
        self.head.prev = None
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # check if the node passed is a head of the list
        if node == self.head:
            # set next head's value as a new head
            self.head = self.head.next
            # set new tail's prev value to None
            self.head.prev = None
        # set old tail's node as a prev of current head
        self.tail.next = node
        # set current head as a next node of this node
        node.prev = self.tail
        # set this node as a new head
        self.tail = node
        # set head prev to None
        self.tail.next = None

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # base case if head 
        if self.head is None:
            # return None
            return None
        # Case 1: if node is a head
        if self.head == node:
            # and if head next is None
            if self.head.next is None:
                # set everything to None (remove from list)
                self.head = None
                self.tail = None
                node = None
                # update length
                self.length -= 1
                return
            # otherwise (if head next is not None)
            else:
                # store next of the head
                nxt = self.head.next
                # set prev of the next to None
                nxt.prev = None
                # set next as a new head
                self.head = nxt
                # updte length
                self.length -= 1
                return
        # case 2: if node's next is not None
        elif node.next is not None:
            # and if node's next is not tail
            if node.next is not self.tail:
                # store node's next
                nxt = node.next
                # store node's prev
                prev = node.prev
                # set next's prev to node's prev
                nxt.prev = prev
                # set prev's next to node's next
                prev.next = nxt
                # set node's next to none
                node.next = None
                # set node's prev to none
                node.prev = None
                # get rid of the node
                node = None
                # update the length
                self.length -= 1
                return
            #otherwise (if the next of the node is tail)
            else:
                # store node's next
                nxt = node.next
                # store node's prev
                prev = node.prev
                # set next's prev to node's prev
                nxt.prev = prev
                # set prev's next to node's next
                prev.next = nxt
                self.tail = nxt
                node.next = None
                node.prev = None
                node = None
                self.length -= 1
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            node.prev = None
            node = None
            self.length -= 1
            return




    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # set max and current starting point (head)
        max = current = self.head
        # while current is not None iterate
        while current:
            # if max value less then current value
            if max.value < current.value:
                # set current value to max value variable
                max.value = current.value
            # update current to next
            current = current.next
        # return max value in a list
        return max.value
        

dll = DoublyLinkedList()
dll.add_to_head(1)
dll.add_to_head(2)
dll.add_to_head(3)
dll.add_to_head(4)
# print(dll.head.value)
dll.add_to_head(5)
# print(dll.head.value)


# print("head, prev and next")
# print(dll.head.value)
# print(dll.head.prev)
# print(dll.head.next.value)
# print("tail, prev and next")
# print(dll.tail.value)
# print(dll.tail.prev.value)
# print(dll.tail.next)
# dll.move_to_front(dll.tail.prev)
# print("new head, prev and next")
# print(dll.head.value)
# print(dll.head.prev)
# print(dll.head.next.value)
dll.delete(dll.head.next)
print(dll.head.next.prev.value)





