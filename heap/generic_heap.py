#!/usr/bin/env python

import os
import sys
sys.path.append(
	os.path.join(
		os.path.dirname(__file__),
		'..'
	)
)
from doubly_linked_list import DoublyLinkedList


class Heap:
	def __init__(self, comparator=lambda x, y: x > y):
		self.storage = DoublyLinkedList()
		self.comparator = comparator

	def insert(self, value):
		self.storage.append(value)
		self._bubble_up(len(self.storage) - 1)

	def delete(self):
		value = self.storage[0]
		if len(self.storage) > 1:
			self.storage[0] = self.storage.remove_from_tail()
		elif len(self.storage) == 1:
			self.storage.remove_from_tail()
		self._sift_down(0)
		return value

	def get_priority(self):
		return self.storage[0]

	def __len__(self):
		return len(self.storage)

	get_size = __len__

	def _swap(self, index_0, index_1):
		(
			self.storage[index_0],
			self.storage[index_1],
		) = (
			self.storage[index_1],
			self.storage[index_0],
		)

	def _bubble_up(self, index):
		parent_index = (index - 1) // 2
		if parent_index < 0:
			return
		# print(f'_bubble_up({index})')
		# print(self.storage)
		# print(f'index {index}: {self.storage[index]}')
		# print(f'parent_index {parent_index}: {self.storage[parent_index]}')
		if self.comparator(self.storage[index], self.storage[parent_index]):
			self._swap(index, parent_index)
			self._bubble_up(parent_index)

	def _sift_down(self, index):
		child_values = list(self.storage[index * 2 + 1:index * 2 + 3])
		if len(child_values) == 0:
			return
		if self.comparator(self.storage[index], max(child_values)):
			return
		if len(child_values) == 1:
			self._swap(index * 2 + 1, index)
		elif self.comparator(child_values[0], child_values[1]):
			self._swap(index * 2 + 1, index)
			self._sift_down(index * 2 + 1)
		else:
			self._swap(index * 2 + 2, index)
			self._sift_down(index * 2 + 2)
