#!/usr/bin/env python

import sys
import os

sys.path.append(
	os.path.join(
		os.path.dirname(__file__),
		'..'
	)
)
from queue_and_stack.dll_queue import Queue
from queue_and_stack.dll_stack import Stack


class DuplicateKeyError(KeyError):
	pass


class BinarySearchNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	# Insert the given value into the tree
	def insert(self, value):
		if value > self.value:
			if self.right is None:
				self.right = BinarySearchNode(value)
			else:
				self.right.insert(value)
		elif value < self.value:
			if self.left is None:
				self.left = BinarySearchNode(value)
			else:
				self.left.insert(value)
		else:
			raise DuplicateKeyError(f'Value "{value}" already exists in tree at node {self}.')

	# Return True if the tree contains the value
	# False if it does not
	def contains(self, value):
		if value == self.value:
			return True
		elif value > self.value and self.right is not None:
			return self.right.contains(value)
		elif value < self.value and self.left is not None:
			return self.left.contains(value)
		else:
			return False

	# Return the maximum value found in the tree
	def get_max(self):
		if self.right is not None:
			return self.right.get_max()
		return self.value

	# Call the function `cb` on the value of each node
	# You may use a recursive or iterative approach
	def for_each(self, cb):
		cb(self.value)
		if self.left is not None:
			self.left.for_each(cb)
		if self.right is not None:
			self.right.for_each(cb)

	# DAY 2 Project -----------------------

	# Print all the values in order from low to high
	# Hint:  Use a recursive, depth first traversal
	def in_order_print(self):
		if self.left is not None:
			self.left.in_order_print()
		print(self.value)
		if self.right is not None:
			self.right.in_order_print()

	# Print the value of every node, starting with the given node,
	# in an iterative breadth first traversal
	def bft_print(self, node):
		children = [node]
		while len(children):
			new_children = []
			for child in children:
				print(child.value)
				if child.left is not None:
					new_children.append(child.left)
				if child.right is not None:
					new_children.append(child.right)
			children = new_children

	# Print the value of every node, starting with the given node,
	# in an iterative depth first traversal
	def dft_print(self, node):
		stack = Stack([node])
		while len(stack):
			node = stack.pop()
			print(node.value)
			if node.right is not None:
				stack.push(node.right)
			if node.left is not None:
				stack.push(node.left)

	# STRETCH Goals -------------------------
	# Note: Research may be required

	# Print Pre-order recursive DFT
	def pre_order_dft(self):
		print(self.value)
		if self.left is not None:
			self.left.pre_order_dft()
		if self.right is not None:
			self.right.pre_order_dft()

	# Print Post-order recursive DFT
	def post_order_dft(self):
		if self.left is not None:
			self.left.post_order_dft()
		if self.right is not None:
			self.right.post_order_dft()
		print(self.value)


class BinarySearchTree(BinarySearchNode):
	pass


