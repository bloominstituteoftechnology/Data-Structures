Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

   Depends on a implementation.

   With queue based on linked list it is **O(1)**. With queue based on an array
   it may be **O(n)** when it needs to rewrite an entire array if there is no
   space left. We can enhance our queue with the max length/size parameter to
   prevent this.

2. What is the runtime complexity of `dequeue`?

   Depends on a implementation.

   With queue based on linked list it is **O(1)**. With queue based on an array
   it is **O(n)** as it needs to shift all elements by one position.

3. What is the runtime complexity of `len`?

   Depends on the implementation.

   Can be **O(1)** with some additional memory (one variable) but can be
   **O(n)** without storing that memory in the actual Queue object. Then the
   method needs to traverse an entire queue that leads to **O(n)**.

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

## Doubly Linked List

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
