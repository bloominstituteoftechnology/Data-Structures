"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
sys.path.append('../stack')
sys.path.append('../queue')
from stack import Stack
from queue import Queue

class BSTNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	# Insert the given value into the tree
	def insert(self, value):
		new_node = BSTNode(value)
		if not self.value:
			self.value = value
		elif value < self.value:
			if not self.left:
				self.left = new_node
			else:
				self.left.insert(value)
		else:
			if not self.right:
				self.right = new_node
			else:
				self.right.insert(value)


	# Return True if the tree contains the value
	# False if it does not
	def contains(self, target):
		if self.value == target:
			return True
		if target < self.value:
			if not self.left:
				return False
			else:
				return self.left.contains(target)
		else:
			if not self.right:
				return False
			else:
				return self.right.contains(target)

	# Return the maximum value found in the tree
	def get_max(self):
		if not self.right:
			return self.value
		else:
			return self.right.get_max()

	# Call the function `fn` on the value of each node
	def for_each(self, fn):
		fn(self.value)
		if self.left is not None:
			self.left.for_each(fn)
		if self.right is not None:
			self.right.for_each(fn)

	# Part 2 -----------------------

	# Print all the values in order from low to high
	# Hint:  Use a recursive, depth first traversal
	def in_order_print(self, node):
		if node:
			self.in_order_print(node.left)
			print(node.value)
			self.in_order_print(node.right)

	# Print the value of every node, starting with the given node,
	# in an iterative breadth first traversal
	def bft_print(self, node):
		# make a queue
		queue = Queue()
		# enqueue the node
		queue.put(node)
		# as long as the queue is not empty
		while queue.qsize() > 0:
			## dequeue from the front of the queue, this is our current node
			current_node = queue.get()
			print(current_node.value)
			## enqueue the kids of the current node on the queue
			if current_node.left:
				queue.put(current_node.left)
			if current_node.right:
				queue.put(current_node.right)

	# Print the value of every node, starting with the given node,
	# in an iterative depth first traversal
	def dft_print(self, node):
		# make a stack
		stack = Stack()
		# push the node on the stack
		stack.push(node)
		# as long as the stack is not empty
		while len(stack) > 0:
			## pop off the stack, this is our current node
			current_node = stack.pop()
			print(current_node.value)
			## put the kids of the current node on the stack
			## (check that they are not None, then put them on the stack)
			if current_node.left:
				stack.push(current_node.left)
			if current_node.right:
				stack.push(current_node.right)

	# Stretch Goals -------------------------
	# Note: Research may be required

	# Print Pre-order recursive DFT
	def pre_order_dft(self, node):
		pass

	# Print Post-order recursive DFT
	def post_order_dft(self, node):
		pass
