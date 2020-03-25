#!/usr/bin/env python

import sys
import os
sys.path.append(
	os.path.join(
		os.path.dirname(__file__),
		'../doubly_linked_list'
	)
)
from doubly_linked_list import DoublyLinkedList


class Queue(DoublyLinkedList):
	enqueue = DoublyLinkedList.add_to_tail
	__len__ = DoublyLinkedList.__len__
	len = __len__

	def dequeue(self):
		if len(self):
			return self.remove_from_head()
		else:
			return None

