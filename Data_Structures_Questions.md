Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

O(1)

2. What is the runtime complexity of `dequeue`?

O(1)

3. What is the runtime complexity of `len`?

O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`?

O(n) 

2. What is the runtime complexity of `contains`?

O(n)

3. What is the runtime complexity of `get_max`? 

O(n)

## Heap

1. What is the runtime complexity of `_bubble_up`?

O(n) due to recursion

2. What is the runtime complexity of `_sift_down`?

O(n) due to recursion

3. What is the runtime complexity of `insert`?

O(n) b/c it invokes bubble up

4. What is the runtime complexity of `delete`?

O(n) b/c it invokes sift down

5. What is the runtime complexity of `get_max`?

O(1) b/c max is stored in real time as heap is updated

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

    in our doubly linked list, our delete function references a specific node so it's an O(1) complexity operation (to invoke the command the node must already be identified, no traversal is needed). for splice in array, the input is an index meaning traversal is also not needed and it is therefore also O(1) complexity. they should perform generally the same.