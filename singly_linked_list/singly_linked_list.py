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

if __name__ == "__main__":
    ll = Node(1)
    ll.set_next(Node(2))
    ll.next.set_next(Node(3))
    ll.next.next.set_next(Node(4))
    ll.next.next.next.set_next(Node(5))