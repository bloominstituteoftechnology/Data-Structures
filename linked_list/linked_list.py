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

	def add_to_tail(self, value):
		node = Node(value)
		print(f"node: {node.get_value()}")
		node.set_next(None)
		if(self.tail == None and self.head == None):
			self.tail = node
			self.head = node
		self.tail.set_next(node)
		self.tail = node

	def remove_head(self):
		if(self.head == None):
			return
		new_head = self.head.get_next()
		self.head = new_head

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


firstLinkedListEver = LinkedList()
firstLinkedListEver.add_to_tail(99)
firstLinkedListEver.add_to_tail(10)
firstLinkedListEver.add_to_tail(3)
firstLinkedListEver.add_to_tail(66)
firstLinkedListEver.add_to_tail(3)
firstLinkedListEver.add_to_tail(34)
# firstLinkedListEver.remove_head()
firstLinkedListEver.contains(firstLinkedListEver.head, 66)
print(f"max: {firstLinkedListEver.get_max()}")
