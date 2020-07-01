class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return (f'{self.data}')

    def get_value(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, updated_next):
        self.next = updated_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        current_node = self.get_head()
        while True:
            if current_node is None:
                return count
            else:
                count += 1
                current_node = current_node.get_next()
        return count

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head

    def add_to_tail(self, data):
        new_node = Node(data)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def add_to_head(self, data):
        new_node = Node(data)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.set_next(self.head)
            self.head = new_node

    def remove_head(self):
        if self.head is None:
            return None
        old_head = self.head

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = old_head.get_next()

        return old_head.get_value()

    def contains(self, data):
        if self.head is None:
            return False

        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return True

            current_node = current_node.get_next()
        return False

    def get_max(self):
        if self.head is None:
            return None

        max = self.head.get_value()
        current_node = self.head

        while current_node is not None:
            if current_node.get_value() > max:
                max = current_node.get_value()

            else:
                current_node = current_node.get_next()

        return max

    def remove_tail(self):
        if self.head is None or self.tail is None:
            return None
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        else:
            current_node = self.head
            tail = self.get_tail()
            while True:
                if current_node is None:
                    break
                next_node = current_node.get_next()
                if next_node is tail:
                    print('popped off!')
                    self.tail = current_node
                    current_node.set_next(None)
                    break
                else:
                    next_node = current_node.get_next()
                    print(f'{current_node}, {next_node}')
                    current_node = next_node
        return tail.get_value()
