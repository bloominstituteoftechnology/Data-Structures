#!/usr/bin/env python

from queue_and_stack.dll_queue import Queue

first = Queue([1, 2, 6, 'George', None])
print(first)
print(list(first[2:]))
another = Queue(reversed(first))
print(another)
print(another.dequeue())
print(another.dequeue())
print(another.dequeue())
another.enqueue(first)
another.extend(first)
print(another)
for item in reversed(another):
	another.append(item)
print(another)
another[0] = Queue(another[:])
print(another)
