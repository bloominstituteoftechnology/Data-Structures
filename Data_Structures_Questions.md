For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `add_to_tail`?
    O(1) constant time since we have a direct reference to the last element
  
    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?
    O(n) linear time, since we would need to traverse every element once

2. What is the runtime complexity of `remove_head`?
    O(1) constant time since we have direct reference to the head element

3. What is the runtime complexity of `contains`?
    O(n) linear time since we traverse every element once

4. What is the runtime complexity of `get_max`?
    O(n) linear time since we traverse every element once

## Queue

1. What is the runtime complexity of `enqueue`?
    O(1) constant time since we have direct access to the head via our LinkedList methods

2. What is the runtime complexity of `dequeue`?
    O(1) constant time since we have direct access to the tail via out LinkedList methods

3. What is the runtime complexity of `len`?
    O(1) constant time since we're tracking our self.size

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
    O(log n) logarithmic time since we must traverse half of all elements

2. What is the runtime complexity of `contains`?
    O(log n) logarithmic time since we must traverse half of all elements

3. What is the runtime complexity of `get_max`? 
    O(log n) logarithmic time since we must traverse at least half of all elements

## Heap

1. What is the runtime complexity of `_bubble_up`?
    O(log n) logarithmic time since we're traversing half of all elements (either left or right branch)

2. What is the runtime complexity of `_sift_down`?
    O(log n) logarithmic time since we're traversing down half of all branches

3. What is the runtime complexity of `insert`?
    O(log n) since we must bubble through half of all branches

4. What is the runtime complexity of `delete`?
    O(log n) since we must sift down half of all branches

5. What is the runtime complexity of `get_max`?
    O(1) constant time since our max heap structure keeps the max value at index[1]

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