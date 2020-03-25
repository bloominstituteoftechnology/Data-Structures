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


class Stack(DoublyLinkedList):
	push = DoublyLinkedList.add_to_head
	__len__ = DoublyLinkedList.__len__
	len = __len__

	def pop(self):
		if len(self):
			return self.remove_from_head()
		else:
			return None
