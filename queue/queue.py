import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
	def __init__(self):
		self.size = 0
		self.storage = LinkedList()

	def enqueue(self, item):
		self.storage.add_to_tail(item)
		self.size = self.storage.get_size()
		return self.size

	def dequeue(self):
		if(self.storage.get_size() == 0):
			print("Your queue is empty")
			return
		head_value = self.storage.head.get_value()
		self.storage.remove_head()
		self.size = self.storage.get_size()
		return head_value

	def len(self):
		return self.storage.get_size()

	
