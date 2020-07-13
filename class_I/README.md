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