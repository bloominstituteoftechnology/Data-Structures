# Lecture I Notes - Data Structures I

## Runtime Complexity

## Linked List
- Compare and contrast linked lists vs arrays(Python lists)
    ```py
    [1,2,3,4,5,6,7] #> contiguous
    ```
    ```py
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> N
    # linked list are a combination of nodes

    class Node:
        value #> the numbers in ex. above
        next #> the arrows in ex. above
    ```
    ```py
    # when iterating through a linked list, `next` can
    # only access a specific Node
    ll = Node(1)
    ll.next = Node(2)
    ll.next.next = Node(3)
    ll.next.next.next = Node(4)
    ll.next.next.next.next = Node(5)
    ```
- Create another class to organize the nodes (before adding `tail`, we have to start from the head of link and traverse all the way to the end of linked list to add new elem)
    ```py
    # Adding a tail brings a constant runtime complexity
    # to the list

    class Node:
        def __init__(self, value, next):
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

        def add_to_tail(self, value):
            # So what do we do if tail is None?

            # These three steps assume that the tail is already
            # referring to a Node
            
            # 1. create the Node from the value
            new_node = Node(value)
            # 2. set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node
            # If self.tail == None, this is not going to work
            self.tail = new_node
    ```
    Adding to tail:
    ```py
    class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def add_to_tail(self, value):
            # 1. create the Node from the value
            new_node = Node(value)

            # What's the rule we want to set to indicate that the linked
            # list is empty?

            # Would it be better to check the head?

            # Lets check both

            # Handle is self.tail is none
            if self.head is None and self.tail is None:
                # in a one-element linked list, we can decide what head and tail
                # should refer to

                # in this case, we can have both refer to the single node
                self.head = new_node
                # set new_node to be the tail
                self.tail = new_node
            else:
                # 2. set the old tail's next to refer to the new Node
                self.tail.set_next(new_node)
                # 3. reassign self.tail to refer to the new Node
                self.tail = new_node
    ```
    removing from linked list (tail):
    ```py
    def remove_tail(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return 

        # if we have a non-empty linked list
        
        # have to start at the head and move down the linked list
        # until we get to the node right before the tail
        # iterate over our linked list
        current = self.head

        # while loop since we dont know how many iterations we'll need (no
        # len property on linked list)
        while current.get_next() i not self.tail:
            # keep iterating
            current = current.get_next()
        # at this point, `current` is the node right before the tail

        # set tail to be None
        val = self.tail.get_value()
        self.tail = None #> this step is not actually needed since we 
        # set tail to current later, but it is here for illustration

        # move self.tail to the Node right before
        self.tail = current
        return val
    ```
    removing from linked list (head):
    ```py
    def remove_head(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return 
        
        # what if we only have single elem in linked list?
        # both head and tail are pointing to the same Node
        if not self.head.get_next():
            head = self.head
            # delete the linked list's head reference
            self.head = None
            # also delete the linked list's tail reference
            self.tail = None
            return head.get_value()

        # if non empty
        val = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val
    ```

    ## Assignment:
    - Work with Stacks and Queues

        - ***Stacks:*** 
        Can think of a stack of dishes: last in is the first out

        - ***Queues:***
        Can think of line in a grocery store: first in, first out