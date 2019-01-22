Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
    - O(1)

2. What is the runtime complexity of `dequeue`?
    - O(1)

3. What is the runtime complexity of `len`?
    - O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
    - O(log n)

2. What is the runtime complexity of `contains`?
    - O(log n)

3. What is the runtime complexity of `get_max`? 
    - O(log n)

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
    - O(1)

2. What is the runtime complexity of `ListNode.insert_before`?
    - O(1)

3. What is the runtime complexity of `ListNode.delete`?
    - O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    - O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    - O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    - O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    - O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    - O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    - O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
    - O(1)
    
    - Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
        - I don't know JS, but deleting a value from the middle of an array would be O(n) whereas dll delete() would only be O(1). Deleting from the middle of an array causes each of the succeeding values in the array to move up one spot in memory. With dlls, it doesn't matter where each of the values is in memory, just that the head and tail of the item to delete, point at each other.