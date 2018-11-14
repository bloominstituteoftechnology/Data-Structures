class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f"{self.data}, {self.next_node}"

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, value):
        if type(value) == Node:
            self.next_node = value


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        return f"{self.head}"

    def insert(self, data):
        # O(1)
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current_node = self.head
        count = 0
        # O(n)
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        return count

    def search(self, data):
        # O(n)
        current_node = self.head
        found = False
        while current_node is not None and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                current_node = current_node.get_next()
            if current_node is None:
                raise ValueError("Node not found")
        return current_node


ll = LinkedList()
ll.insert("Brian")
ll.insert("Shawn")
ll.insert("Doris")
print(ll)
print(ll.size())
print(ll.search('Doris'))
