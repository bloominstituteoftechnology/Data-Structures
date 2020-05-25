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


# Array Implement
class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = []
        self.queue = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def print_queue(self):
        for value in self.queue:
            print(value)


my_q = Queue()
print('Length Result equals:', my_q.__len__())
for i in range(10):
    my_q.enqueue(i)
my_q.print_queue()
print(my_q.peek())
my_q.dequeue()
my_q.print_queue()

# example of a for loop
# def for_loop_n(n):
#    for i in range(n):
#        print(i)
# def for_loop_constant():
#    for i in range(10):
#        print(i)
