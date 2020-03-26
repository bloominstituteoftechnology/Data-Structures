
from itertools import islice

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:

	def __init__(self, value, prev_node=None, next_node=None):
		self.value = value
		self.prev_node = prev_node
		self.next_node = next_node

	"""Wrap the given value in a ListNode and insert it
	after this node. Note that this node could already
	have a next node it is point to."""
	def insert_after(self, value):
		current_next = self.next_node
		self.next_node = ListNode(value, self, current_next)
		if current_next:
			current_next.prev_node = self.next_node

	"""Wrap the given value in a ListNode and insert it
	before this node. Note that this node could already
	have a previous node it is point to."""
	def insert_before(self, value):
		current_prev = self.prev_node
		self.prev_node = ListNode(value, current_prev, self)
		if current_prev:
			current_prev.next_node = self.prev_node

	"""Rearranges this ListNode's previous and next pointers
	accordingly, effectively deleting this ListNode."""
	def delete(self):
		if self.prev_node:
			self.prev_node.next_node = self.next_node
		if self.next_node:
			self.next_node.prev_node = self.prev_node

	def __hash__(self):
		return hash(value)

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
	def __init__(self, iterable=None):
		self.head = None
		self.tail = None
		self.length = 0
		if iterable is not None:
			self.extend(iterable)

	"""Wraps the given value in a ListNode and inserts it
	as the new head of the list. Don't forget to handle
	the old head node's previous pointer accordingly."""
	def add_to_head(self, value):
		new_node = ListNode(value)
		self.length += 1
		if not self.head and not self.tail:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next_node = self.head
			self.head.prev_node = new_node
			self.head = new_node

	"""Removes the List's current head node, making the
	current head's next node the new head of the List.
	Returns the value of the removed Node."""
	def remove_from_head(self):
		value = self.head.value
		self.delete(self.head)
		return value

	"""Wraps the given value in a ListNode and inserts it
	as the new tail of the list. Don't forget to handle
	the old tail node's next pointer accordingly."""
	def add_to_tail(self, value):
		new_node = ListNode(value)
		self.length += 1
		if not self.head and not self.tail:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.prev_node = self.tail
			self.tail.next_node = new_node
			self.tail = new_node

	"""Removes the List's current tail node, making the
	current tail's previous node the new tail of the List.
	Returns the value of the removed Node."""
	def remove_from_tail(self):
		value = self.tail.value
		self.delete(self.tail)
		return value

	"""Removes the input node from its current spot in the
	List and inserts it as the new head node of the List."""
	def move_to_front(self, node):
		if node is self.head:
			return
		value = node.value
		self.delete(node)
		self.add_to_head(value)

	"""Removes the input node from its current spot in the
	List and inserts it as the new tail node of the List."""
	def move_to_end(self, node):
		if node is self.tail:
			return
		value = node.value
		self.delete(node)
		self.add_to_tail(value)

	"""Removes a node from the list and handles cases where
	the node was the head or the tail"""
	def delete(self, node):
		# TODO: Catch errors if list is empty or node is not in list
		# For now assumine node is in list
		self.length -= 1
		# if head and tail
		if self.head is self.tail:
			self.head = None
			self.tail = None
		# if head
		elif node is self.head:
			self.head = self.head.next_node
			node.delete()

		# if tail
		elif node is self.tail:
			self.tail = self.tail.prev_node
			node.delete()
		else:
			# if regular node
			node.delete()

	"""Returns the highest value currently in the list"""
	def get_max(self):
		# Loop through all nodes, looking for biggest value
		# TODO: Error checking
		if not self.head:
			return None
		max_value = self.head.value
		current = self.head
		while current:
			if current.value > max_value:
				max_value = current.value
			current = current.next_node

		return max_value

	def get_node_by_value(self, value):
		for index, node in enumerate(self._iter_nodes()):
			if node.value == value:
				return node
		return None

	def index(self, value):
		for index, node_value in enumerate(self):
			if node_value == value:
				return index
		return -1

	def extend(self, iterable):
		for value in iterable:
			self.append(value)
		return self

	def _raise_indexerror(self):
		raise IndexError(f'{self.__class__.__name__} index out of range')

	def _raise_typeerror(self):
		raise TypeError(f'{self.__class__.__name__} indices must be integers or slices, not float')

	def _get_node_at_index(self, index):
		# Future improvements:
		# Iterate from the tail if key > len // 2
		if not isinstance(index, int):
			self._raise_typeerror
		if abs(index) > self.length or index == self.length:
			self._raise_indexerror()

		if index < 0:
			index = self.length + index
		node = self.head
		while index > 0:
			node = node.next_node
			index -= 1
		return node

	def _iter_nodes(self):
		node = self.head
		for _ in range(self.length):
			yield node
			node = node.next_node

	def __getitem__(self, index):
		if isinstance(index, slice):
			indices = index.indices(self.length)
			return islice(self, *indices)

		else:
			return self._get_node_at_index(index).value

	def __setitem__(self, index, value):
		self._get_node_at_index(index).value = value

	def __delitem__(self, index):
		self._get_node_at_index(index).delete()

	def __iter__(self):
		for node in self._iter_nodes():
			yield node.value

	def __reversed__(self):
		node = self.tail
		for _ in range(self.length):
			yield node.value
			node = node.prev_node

	def __str__(self):
		return str(list(self))

	def __repr__(self):
		return list(self).__repr__()

	def __len__(self):
		return self.length

	def __eq__(self, other):
		if len(self) != len(other):
			return False
		for self_value, other_value in zip(self, other):
			if self_value != other_value:
				return False
		return True

	append = add_to_tail
	pop = remove_from_tail
