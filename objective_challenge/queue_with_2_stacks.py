
class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop() if self.out_stack else False

    def len(self):
        return len(self.in_stack), len(self.out_stack)

queue = Queue()

print(queue.dequeue())

queue.enqueue(5)
queue.enqueue(8)
queue.enqueue(13)

print(queue.len())

print(queue.dequeue())

print(queue.len())

queue.enqueue(5)
queue.enqueue(8)

print(queue.len())

print(queue.dequeue())

print(queue.len())
