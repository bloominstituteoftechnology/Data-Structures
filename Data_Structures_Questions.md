Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
   O(1) runtime because it can access the last element to add a new one

2. What is the runtime complexity of `dequeue`?
   O(1) runtime because it can access the first element and remove it

3. What is the runtime complexity of `len`?
   O(1) runtime because it is stored as a property of the queue

## Binary Search Tree

1. What is the runtime complexity of `insert`?
   O(log n) because it divides by half n with every operation
2. What is the runtime complexity of `contains`?
   O(log n) because it divides by half n with every operation
3. What is the runtime complexity of `get_max`?
   O(log n) because it divides by half n with every operation

## Heap

1. What is the runtime complexity of `_bubble_up`?
   O(log n) because it divides by half n with every operation

2. What is the runtime complexity of `_sift_down`?
   O(log n) because it divides by half n with every operation

3. What is the runtime complexity of `insert`?
   O(log n) because it calls bubble up after inserting

4. What is the runtime complexity of `delete`?
   O(log n) because it calls shift down after deleting

5. What is the runtime complexity of `get_max`?
   O(1) because it returns the item at index 0

## Doubly Linked List

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
   O(n) because it has to traverse the entire list
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
   O(n) because it has to traverse the entire list
10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(1)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    The `delete` methon in a linked list does not need to move over the elements. It has a better runtime than the JS `Array.splice` method because the splice method would need to move over the elements once it has deleted one. The `delete` function of a linked list generally performs better
