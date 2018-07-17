For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `add_to_tail`?

The run-time complexity is O(1).

    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?

    Run-time complexity is O(n), because it becomes necessary to traverse the linked-list to find the last node in the list to update the `next_node` property of that list.

2. What is the runtime complexity of `remove_head`?

O(1). My implementation only has reassignments.

3. What is the runtime complexity of `contains`?

O(n). The method needs to traverse each node and check the value of each node. It's possible this can be done faster than O(n), and is likely it will, but we're concerned with the *worst-case* scenario.

4. What is the runtime complexity of `get_max`?

O(n). Unlike `contains`, the implementation requires traversing through the entire list each and every time to get and confirm the max value.

## Queue

1. What is the runtime complexity of `enqueue`?
O(1)

2. What is the runtime complexity of `dequeue`?
O(1)

3. What is the runtime complexity of `len`?
O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
O(log n)

2. What is the runtime complexity of `contains`?
O(log n)

3. What is the runtime complexity of `get_max`? 
O(log n)

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
O(1)

2. What is the runtime complexity of `ListNode.insert_before`?
O(1)

3. What is the runtime complexity of `ListNode.delete`?
O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    DoublyLinkedList method would perform better, because it's time complexity is O(1), in contrasts with JS `Array.splice`, which is complexity O(n). The DoublyLinkedList only needs to make a few reassignments, which are all done in constant time, whereas splice needs to create a new array with all the elemenets minus the elements that were spliced out. 