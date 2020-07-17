class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    """LL class"""
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        """
        Reverse the contents of the list using recursion, not a loop
        """
        if self.head is None:
            return None
        
        self.head = node
        current = self.head
        nn = current.next_node

        while nn is not None:
            prev = current
            current = nn
            nn = current.next_node
            current.next_node = prev

            if nn is None:
                self.head = current

        # # Start at head node (no prev no next)
        # if prev is None and current.next_node is None:
        #     self.head = node
        
        # # if current node has a next
        # if current.get_next():
        #     # Make next node the new head
        #     self.head = current.get_next()
        #     # Make current node the new next
        #     self.head.set_next(current)
                

if __name__ == "__main__":

    ll = LinkedList()

    ll.add_to_head(1)
    ll.add_to_head(2)
    ll.add_to_head(3)
    ll.add_to_head(4)
    ll.add_to_head(5)

    # breakpoint()
    ll.reverse_list(ll.head, None)
    print(ll.head.value) #> 1
    print(ll.head.get_next().value) #> 2
    print(ll.head.get_next().get_next().value) #> 3


    # breakpoint()