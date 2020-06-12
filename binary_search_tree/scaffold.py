#> Check <PASS>

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# from sys import path
# path.append("../")

class Queue:                                                               #<<<
    def __init__(self):
        self._stack = 0
        self._storage = singleLinkedList()
    
    def __len__(self):
        return self._stack

    def enqueue(self, value):
        self._storage.add_to_tail(value)
        self._stack += 1

    def dequeue(self):
        if self.__len__() > 0:
            self._stack -= 1
            return self._storage.remove_head()
        if self.__len__() <= 0:
            return


class Stack():                                                             #<<<
    def __init__(self):
        self._stack = 0
        self._size = singleLinkedList()

    def __len__(self):
        return self._stack

    def push(self, value):
        self._size.add_to_tail(value)
        self._stack += 1

    def pop(self):
        if self.__len__() < 1:
            return None
        else:
            self._stack -= 1
            return self._size.remove_tail()


class Node():                                                              #<<<
    def __init__(self, value, next=None):
        self._value = value
        self._next_node = next
    
    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_node

    def set_next(self, new_next):
        self._next_node = new_next

    @property
    def value(self):
        return self._value
    @property
    def next_node(self):
        return self._next_node

    @value.setter
    def value(self, x):
        self._head = x
    @next_node.setter
    def next_node(self, x):
        self._next_node = x


class singleLinkedList():                                                  #<<<
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head
    @property
    def tail(self):
        return self._tail

    @head.setter
    def value(self, x):
        self._head = x
    @tail.setter
    def left(self, x):
        self._tail = x

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self._head and not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.set_next(new_node)
            self._tail = new_node

    def remove_tail(self):
        if self._tail is None:
            return None
        data = self._tail.get_value()
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.get_next() != self._tail:
                current = current.get_next()
            self._tail = current
        return data

    def remove_head(self):
        if self._head is None:
            return None
        data = self._head.get_value()
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.get_next()
        return data

    def contains(self, data):
        if not self._head:
            return False
        current = self._head 
        while current is not None:
            if current.get_value() == data:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        if self._head is None:
            return None
        max_so_far = self._head.get_value()
        current = self._head.get_next()
        while current is not None:
            if current.get_value() > max_so_far:
                max_so_far = current.get_value()
            current = current.get_next()
        return max_so_far


class ListNode:                                                            #<<<
    def __init__(self, value, prev=None, next=None):
        self._value = value
        self._prev = prev
        self._next = next

    @property
    def value(self):
        return self._value
    @property
    def prev(self):
        return self._prev
    @property
    def next(self):
        return self._next

    @value.setter
    def value(self, x):
        self._value = x
    @prev.setter
    def prev(self, x):
        self._prev = x
    @next.setter
    def next(self, x):
        self._next = x

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self._next
        self._next = ListNode(value, self, current_next)
        if current_next:
            current_next._prev = self._next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self._prev
        self._prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev._next = self._prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self._prev:
            self._prev._next = self._next
        if self._next:
            self._next._prev = self._prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class doubleLinkedList:                                                    #<<<
    def __init__(self, node=None):
        self._head = node
        self._tail = node
        self._length = 1 if node is not None else 0

    def __len__(self):
        return self._length
    
    @property
    def head(self):
        return self._head
    @property
    def tail(self):
        return self._tail
    @property
    def length(self):
        return self._length

    @head.setter
    def head(self, x):
        self._head = x
    @tail.setter
    def tail(self, x):
        self._tail = x
    @length.setter
    def length(self, x):
        self._length = x

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        self._length += 1
        if not self._head and not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
            self._head._prev = new_node
            self._head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self._head._value
        self.delete(self._head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self._length += 1
        if not self._head and not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            new_node._prev = self._tail
            self._tail._next = new_node
            self._tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self._tail._value
        self.delete(self._tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self._head:
            return
        value = node._value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self._tail:
            return
        value = node._value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self._length -= 1

        if self._head is self._tail:
            self._head = None
            self._tail = None
        elif node is self._head:
            self._head = node._next
            node.delete()
        elif node is self._tail:
            self._tail = node._prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""
    def get_max(self):
        # Loop through all nodes, looking for biggest value
        if not self._head:
            return None
        max_value = self._head._value
        current = self._head
        while current:
            if current._value > max_value:
                max_value = current._value
            current = current._next

        return max_value


if __name__ == "__main__":
    pass

# import pkgutil
# search_path = ['.'] # set to None to see all modules importable from sys.path
# all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
# print(all_modules)