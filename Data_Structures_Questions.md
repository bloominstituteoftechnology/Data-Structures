Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
 - Runtime of O(1) because nothing has to be shifted, we only change pointers to the new tail.

2. What is the runtime complexity of `dequeue`?
- Runtime is O(1) because we only change pointers to the new head.

3. What is the runtime complexity of `len`?
- Runtime is O(1) if we are keeping track of the length as the list grows; otherwise, it would be
O(n) because we would have to iterate through the list to count the elements.

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
- Runtime is O(n) because we have to iterate though the list to find the node to insert after.

2. What is the runtime complexity of `ListNode.insert_before`?
- Runtime is O(n) because we have to iterate though the list to find the node to insert before.

3. What is the runtime complexity of `ListNode.delete`?
- Runtime is O(n) because we have to iterate though the list to find the node to delete.

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
- Runtime is O(1) because we are only updating pointers to the head.

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
- Runtime is O(1) because we are only updating pointers to the head.

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
- Runtime is O(1) because we are only updating pointers to the tail.

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
- Runtime is O(1) because we are only updating pointers to the tail.

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
- If we are moving the value at the tail to the front then runtime is O(1);
otherwise, runtime is O(n) because we have to iterate to the item that needs
to be moved to the front.

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
- If we are moving the value at the head to the tail then runtime is O(1);
otherwise, runtime is O(n) because we have to iterate to the item that needs
to be moved to the end.

10. What is the runtime complexity of `DoublyLinkedList.delete`?
- Runtime is O(n) because we have to iterate through the list to find the item to delete.

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    -- Runtime of Array.splice is O(n), so both perform the same.