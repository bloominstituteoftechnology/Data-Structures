# A -> B -> C -> D -> 0
# D -> C -> B -> A -> 0
# A <- B <- C <- D -> 0


def reverse_iterative(self):

    previous = None
    current = self.head

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    self.head = previous


def reverse_recursive(self):

    def _reverse_recursive(current, previous):
        if current is None:
            return previous

        next = current.next
        current.next = previous
        previous = current
        current = next
        return _reverse_recursive(current, previous)

    self.head = _reverse_recursive(current=self.head, previous=None)


def reverse_list(self, node, prev):

    # If there is no node or only one node in the list
    if self.head is None or self.head.next_node is None:
        return self.head

    # If there is more than one node in the list
    if node.next_node:
        self.reverse_list(node.next_node, node)

    # Once we reach the end of the list the node.next_node is None
    if node.next_node is None:
        self.head = node

    node.next_node = prev
