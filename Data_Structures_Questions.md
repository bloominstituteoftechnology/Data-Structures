For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `add_to_tail`?
    1. O(1)

    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?
        O(1)

2. What is the runtime complexity of `remove_head`?
    1. O(1)

3. What is the runtime complexity of `contains`?
    1. O(n)

4. What is the runtime complexity of `get_max`?
    1. O(n)

## Queue

1. What is the runtime complexity of `enqueue`?
    1. O(1)

2. What is the runtime complexity of `dequeue`?
    1. O(1)

3. What is the runtime complexity of `len`?
    1. O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`?
    1. O(log n)

2. What is the runtime complexity of `contains`?
    1. O(log n)

3. What is the runtime complexity of `get_max`?
    1. O(log n)

## Heap

1. What is the runtime complexity of `_bubble_up`?
    O(log n)

2. What is the runtime complexity of `_sift_down`?
    O(log n)

3. What is the runtime complexity of `insert`?
    O(log n)

4. What is the runtime complexity of `delete`?
    O(log n)

5. What is the runtime complexity of `get_max`?
    O(1)

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