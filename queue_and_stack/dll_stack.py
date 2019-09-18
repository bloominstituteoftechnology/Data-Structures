import sys

sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList
from doubly_linked_list.doubly_linked_list import DoublyLinkedList


class Stack:
	def __init__(self):
		self.size = 0
		# Why is our DLL a good choice to store our elements?
		self.storage = DoublyLinkedList()

	def push(self, value):
		self.size += 1
		self.storage.add_to_head(value)

	def pop(self):
		if self.len() > 0:
			self.size -= 1
			val = self.storage.head.value
			self.storage.remove_from_head()
			return val
		return None

	def len(self):
		return self.storage.__len__()
