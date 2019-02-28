Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
- constant 
2. What is the runtime complexity of `dequeue`?
- constant 
3. What is the runtime complexity of `len`?
- linear

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
- log n
2. What is the runtime complexity of `contains`?
- log n
3. What is the runtime complexity of `get_max`? 
- constant 

## Heap

1. What is the runtime complexity of `_bubble_up`?
- linear  
2. What is the runtime complexity of `_sift_down`?
- linear 
3. What is the runtime complexity of `insert`?
- linear
4. What is the runtime complexity of `delete`?
- linear 
5. What is the runtime complexity of `get_max`?
- constant 

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
- linear
2. What is the runtime complexity of `ListNode.insert_before`?
- lineat
3. What is the runtime complexity of `ListNode.delete`?
- linear
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
- constant
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
- constant
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
- constant
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
- constant
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
- O(n+1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
- linear
10. What is the runtime complexity of `DoublyLinkedList.delete`?
- Linear 
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    - Generally, array method is much faster because it has access directly into the index