Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

O(n) in my current implementation. Lists are slow. Inserting or deleting elements requires shifting all other elements by 1. Python's standard library dequeue object supports adding and removing elements from either end with O(1) runtime, so that's much faster.

2. What is the runtime complexity of `dequeue`?

O(n) in my current implementation. Lists are slow. Inserting or deleting elements requires shifting all other elements by 1. Python's standard library dequeue object supports adding and removing elements from either end with O(1) runtime, so that's much faster.

3. What is the runtime complexity of `len`?

same as 2 and 3 since we're using a list

## Binary Search Tree

1. What is the runtime complexity of `insert`?

When inserting elements to the left of child, all previous elements much be traversed. This is O(n) in the worst case.

2. What is the runtime complexity of `contains`?

O(n)

3. What is the runtime complexity of `get_max`?

For a sorted and balanced binary tree one single path is traversed: complexity of O(log(n)).

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
