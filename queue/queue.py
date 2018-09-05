import sys

# sys.path.append('C://Users//Vimal//Documents//LambdaSchool//Data-Structures//linked_list')
sys.path.append('../linked_list')

from linked_list import LinkedList

class Queue:
	def __init__(self):
		self.size = 0
		self.storage = LinkedList()

	def enqueue(self, item):
		self.storage.add_to_tail(item)
		self.size += 1
  
	def dequeue(self):
		if self.size > 0:
			self.size -= 1
		return self.storage.remove_head()


	def len(self):
		return self.size


#Local Tests
# q = Queue()

# q.enqueue(100)
# print('\n 1st write')
# print(q.storage.head.get_value())
# print(q.storage.head.get_next())

# q.enqueue(101)
# print('\n 2nd write')
# print(q.storage.head.get_value())
# print(q.storage.head.get_next().get_value())

# q.enqueue(105)
# print('\n 3rd write')
# print(q.storage.head.get_value())
# print(q.storage.head.get_next().get_value())
# print(q.storage.head.get_next().get_next().get_value())

# print('\n 1 deq')
# print(q.dequeue())

