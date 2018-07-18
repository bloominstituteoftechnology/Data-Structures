For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `add_to_tail`?
R// O(1)
  
    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?
R//In that case the function would have to go through the list from head to tail, so it would be O(n)

2. What is the runtime complexity of `remove_head`? R// O(1)

3. What is the runtime complexity of `contains`?R// O(n)

4. What is the runtime complexity of `get_max`? R// O(n)


## Queue
 
1. What is the runtime complexity of `enqueue`? R// O(1)

2. What is the runtime complexity of `dequeue`? R// O(1) 
 
3. What is the runtime complexity of `len`? R// O(1)


## Binary Search Tree

1. What is the runtime complexity of `insert`? R// log(n) 

2. What is the runtime complexity of `contains`? R// log(n) 

3. What is the runtime complexity of `get_max`? R// log(n) 

## Heap

1. What is the runtime complexity of `_bubble_up`? R// log(n) 

2. What is the runtime complexity of `_sift_down`? R// log(n) 

3. What is the runtime complexity of `insert`? R// log(n) 

4. What is the runtime complexity of `delete`? R// log(n) 

5. What is the runtime complexity of `get_max`? R// O(1)

## [Stretch Goal] Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`? R// 

2. What is the runtime complexity of `ListNode.insert_before`? R// 

3. What is the runtime complexity of `ListNode.delete`? R// 

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`? R// 

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`? R// 

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`? R// 

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`? R// 

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`? R// 

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`? R// 

10. What is the runtime complexity of `DoublyLinkedList.delete`? R// 

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better? R// 