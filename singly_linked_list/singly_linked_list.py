class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

class LinkedList:
	def __init__(self, node=None):
		self.head = node
		self.tail = node

	def add_to_tail(self, value):
		new_node = Node(value)
		if self.tail:
			self.tail.next = new_node
		else:
			self.head = new_node

		self.tail = new_node

	def contains(self, value):
		current = self.head

		while current is not None:
			if current.value == value:
				return True
			current = current.next
		return False

	def remove_head(self):
		val = self.head.value

		if self.head.next is not None:
			self.head = self.head.next
		else:
			self.head = None

		return val

	def get_max(self):
		this = self.head
		if this is None:
			return None

		val = self.head.value
		while this is not None:
			if this.value > val:
				val = this.value
			this = this.next
		return val
