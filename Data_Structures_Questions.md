Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push`? O(1)

2. What is the runtime complexity of `pop`? O(1)

3. What is the runtime complexity of `len`? O(n)

## Queue

1. What is the runtime complexity of `enqueue`? O(1)

2. What is the runtime complexity of `dequeue`? O(1)

3. What is the runtime complexity of `len`? O(n)

## Binary Search Tree

1. What is the runtime complexity of `insert`? O(logn)

2. What is the runtime complexity of `contains`? O(logn)

3. What is the runtime complexity of `get_max`? O(logn)

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`? O(1)

2. What is the runtime complexity of `ListNode.insert_before`? O(1)

3. What is the runtime complexity of `ListNode.delete`? O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`? O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`? O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`? O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`? O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`? O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`? O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`? O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    I'm not familiar, but I'm guessing it's O(n), where if the first item is removed, every item has to be "moved down a slot" in memory in order.
