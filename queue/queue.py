class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.size = 0
        # entry point of the queue (back of queue) == HEAD of Node list
        self.storage = Node()

    # enqueue should add an item to the back of the queue
    def enqueue(self, item):
        # no items in storage => first item in queue
        if not self.storage.value:
            new_node = Node(item)
            self.storage = new_node
            print(f'storage: {self.storage.value}')
        # if there are other items in the queue
        # add new node and give it ref to previous Head node
        else:
            # create new Node to add to queue
            new_node = Node(item)
            print(f'prev storage: {self.storage.value}')
            # connect new Node to previous HEAD node
            new_node.next_node = self.storage
            # make new Node new HEAD node
            self.storage = new_node
            print(f'storage: {self.storage.value}')

        # increase the size of the queue
        self.size += 1

    # dequeue should remove and return an item from the front of the queue
    def dequeue(self):
        pass

    # len returns the number of items in the queue
    def len(self):
        return self.size


q = Queue()
print(f'first len: {q.len()} ...should be 0')
q.enqueue(10)
print(f'add item: {q.len()} ..should be 1')
q.enqueue(20)


class Queue_Array:
    def __init__(self):
        self.size = 0
        self.storage = []

    def enqueue(self, item):
        self.storage.insert(0, item)

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        else:
            return self.storage.pop()

    def len(self):
        return len(self.storage)
