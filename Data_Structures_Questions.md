For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `add_to_tail`?
  
    O(1); Constant
  
    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?

      O(n); Linear

2. What is the runtime complexity of `remove_head`?

    O(1); Constant

3. What is the runtime complexity of `contains`?

    O(n); Linear

4. What is the runtime complexity of `get_max`?

    - If function searches for the max value each time it is called: O(n); Linear
    - If the max value is updated each time a node is added to the list: O(1); Constant

## Queue

1. What is the runtime complexity of `enqueue`?

    O(1); Constant

2. What is the runtime complexity of `dequeue`?

    O(1); Constant

3. What is the runtime complexity of `len`?

    O(1); Constant

## Binary Search Tree

1. What is the runtime complexity of `insert`?

    O(log n); Logarithmic

2. What is the runtime complexity of `contains`?

    O(log n); Logarithmic

3. What is the runtime complexity of `get_max`? 

    O(log n); Logarithmic

## Heap

1. What is the runtime complexity of `_bubble_up`?

    O(log n); Logarithmic

2. What is the runtime complexity of `_sift_down`?

    O(log n); Logarithmic

3. What is the runtime complexity of `insert`?

    O(log n); Logarithmic

4. What is the runtime complexity of `delete`?

    O(log n); Logarithmic

5. What is the runtime complexity of `get_max`?

    O(1); Constant

## [Stretch Goal] Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

    O(1); Constant

2. What is the runtime complexity of `ListNode.insert_before`?

    O(1); Constant

3. What is the runtime complexity of `ListNode.delete`?

    O(1); Constant

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

    O(1); Constant

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

    O(1); Constant

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

    O(1); Constant

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

    O(1); Constant

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

    O(1); Constant

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

    O(1); Constant

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    O(1); Constant

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    A doubly linked list will perform better. Its runtime complexity for a delete is O(1) while JavaScript's `Array.splice` method is O(n).