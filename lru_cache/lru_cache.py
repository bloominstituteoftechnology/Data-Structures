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
from doubly_linked_list import DoublyLinkedList


class LRUCache:
	"""
	Our LRUCache class keeps track of the max number of nodes it
	can hold, the current number of nodes it is holding, a doubly-
	linked list that holds the key-value entries in the correct
	order, as well as a storage dict that provides fast access
	to every node stored in the cache.pass
	"""
	def __init__(self, limit=10):
		self.limit = limit
		self.data = {}
		self.expiration_queue = Queue()

	"""
	Retrieves the value associated with the given key. Also
	needs to move the key-value pair to the end of the order
	such that the pair is considered most-recently used.
	Returns the value associated with the key or None if the
	key-value pair doesn't exist in the cache.
	"""
	def get(self, key):
		if key in self.data:
			key_node = self.expiration_queue.get_node_by_value(key)
			self.expiration_queue.move_to_end(key_node)
			return self.data[key]
		else:
			return None

	"""
	Adds the given key-value pair to the cache. The newly-
	added pair should be considered the most-recently used
	entry in the cache. If the cache is already at max capacity
	before this entry is added, then the oldest entry in the
	cache needs to be removed to make room. Additionally, in the
	case that the key already exists in the cache, we simply
	want to overwrite the old value associated with the key with
	the newly-specified value.
	"""
	def set(self, key, value):
		if key in self.data:
			key_node = self.expiration_queue.get_node_by_value(key)
			self.expiration_queue.move_to_end(key_node)
		else:
			self.expiration_queue.enqueue(key)
			if len(self.expiration_queue) > self.limit:
				del self.data[self.expiration_queue.dequeue()]
		self.data[key] = value
