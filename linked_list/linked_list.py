# Viva!
"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next_node = next_node

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def add_to_tail(self, value):
		node = Node(value)
		print(f"node: {node.get_value()}")
		node.set_next(None)
		if(self.tail == None and self.head == None):
			self.tail = node
			self.head = node
		self.tail.set_next(node)
		self.tail = node
		print("how many times calling increment???????")
		self.increment_size()
		print(f"size:::::::: {self.get_size()}")

	def increment_size(self):
		self.size += 1

	def decrement_size(self):
		self.size -= 1

	def get_size(self):
		return self.size

	def remove_head(self):
		if(self.head == None):
			return
		new_head = self.head.get_next()
		self.head = new_head
		self.decrement_size()

	def contains(self, li, value):
		if(li.get_next() ==  None):
			return False
		if(li.get_value() == value):
			print(f"found it: {value}")
			return True
		return self.contains(li.get_next(), value)

	def get_max(self):
		curr_node = self.head
		max = curr_node.get_value()
		while(curr_node.get_next() != None):
			next_node = curr_node.get_next()
			if(next_node.get_value() > max):
				max = next_node.get_value()
			curr_node = next_node
			next_node = curr_node.get_next()
		return max

