For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `add_to_tail`?

    O(c) - nothing changes based on the input

    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?

    Without a reference to the tail, it would require traversing the list to get to the last node which would increase it to o(n), as it would increase as the list got larger

2. What is the runtime complexity of `remove_head`?

  O(c), there is no input to change how the code will execute, and the length of
  the list will not change anything

3. What is the runtime complexity of `contains`?

  O(n), as the list increases, the more evaluations the code might have to perform

4. What is the runtime complexity of `get_max`?

  O(n), same as contains

## Queue

1. What is the runtime complexity of `enqueue`?

  O(c), it uses linked list's add_to_tail, only adding a constant change for recording size

2. What is the runtime complexity of `dequeue`?

  O(c), same as above

3. What is the runtime complexity of `len`?

  O(c), only returns a stored value

## Binary Search Tree

1. What is the runtime complexity of `insert`?

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`?

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## [Stretch Goal] Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
