Answer the following questions for each of the data structures you implemented as part of this project.

## Stack (SLL)

1. What is the runtime complexity of `push`?\
   O(1)
2. What is the runtime complexity of `pop`?\
   O(1)
3. What is the runtime complexity of `len`?\
   O(1). It's stored in the class as a variable, not calculated on demand.

## Queue (DLL)

1. What is the runtime complexity of `enqueue`?\
   O(1)
2. What is the runtime complexity of `dequeue`?\
   O(1)
3. What is the runtime complexity of `len`?\
   O(1). It's stored in the class as a variable, not calculated on demand.

## Binary Search Tree

1. What is the runtime complexity of `insert`? \
O(log n) average, O(n) worst case.
2. What is the runtime complexity of `contains`?\
O(log n) average, O(n) worst case.
3. What is the runtime complexity of `get_max`?\
O(log n) average, O(n) worst case.

## Heap

1. What is the runtime complexity of `_bubble_up`?\
   O(log n)
2. What is the runtime complexity of `_sift_down`?\
   O(log n)
3. What is the runtime complexity of `insert`?\
   O(log n)
4. What is the runtime complexity of `delete`?\
   O(log n)
5. What is the runtime complexity of `get_max`?\
   O(1)

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?\
   O(1)
2. What is the runtime complexity of `ListNode.insert_before`?\
   O(1)
3. What is the runtime complexity of `ListNode.delete`?\
   O(1)
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?\
   O(1)
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?\
   O(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?\
   O(1)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?\
   O(1)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?\
   O(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?\
   O(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?\
    It should be O(1).\
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?\
    JS is not my thing, but I understand it's O(n) worst case.
