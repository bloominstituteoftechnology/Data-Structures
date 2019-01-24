Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
   O(1) Constant time, because it's just adding a next_node value to the tail.
2. What is the runtime complexity of `dequeue`?
   O(1) Constant time, because it's making the head next_node the new head and removing the current head
3. What is the runtime complexity of `len`?
   O(1) Constant time, because we're incrementing or decrementing the size value with each call of `enqueue` or `dequeue`. So, it doesn't have to run through entire list and count whenever `len` is called

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
   O(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
   O(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(1)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
