
class LinkedList:
	def __init__(self):
		self.head = None

	def add_to_end(self, value):
		new_node = Node(value)

		if not self.head:
			self.head = new_node

		else:
			# this doesn't work, have to traverse
			# self.head.set_next(new_node)
			# iterate thru linked list here
			current = self.head
			# so while we haven't reached end of the list
			while current.get_next() is not None:
				current = current.get_next()
			# at end of traversal we set 
			current.set_next(new node)

	def remove_from_head(self):
		# same pattern as above, return nothing if empty
		if not self.head:
			return None
		# if it's not empty? return value at current head 
		else:
			# want to get value at current head
			value = self.head.get_value()
			# move reference from head to next thing in LL 
			# because this is a 1 directional LL, we can no longer access the old head

			self.head = self.head.get_next()
			# and then we return the value whose pointer was removed
			return value 