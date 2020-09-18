Answer the following questions for each of the data structures you implemented as part of this project.

### Running for linked lists and lists
Looking at speeds for adding and removing items \
- Adding 10000 elements to list took 0.0015099048614501953 seconds
- Adding 10000 elements to linked list took 0.022647857666015625 seconds
- List pop from front took 0.016231775283813477 seconds
- Linked list remove from front took 0.01629805564880371 seconds

## Stack

1. What is the runtime complexity of `push` using a list?
    This should be a constant time O(n). Since you are just adding to the beginning of the list.

2. What is the runtime complexity of `push` using a linked list?
    This should be a constant time O(1). Since you are just adding to the beginning of the list.

3. What is the runtime complexity of `pop` using a list?
    This should also be constant time O(n), because you are removing from the tail.

4. What is the runtime complexity of `pop` using a linked list?
    This should also be constant time O(n), because you are removing from the tail.

5. What is the runtime complexity of `len` using a list?
    The run time complexity of checking the len is linear time because it has to count each piece of the list

6. What is the runtime complexity of `len` using a linked list?
    The run time complexity of checking the len is linear time because it has to count each piece of the list


## Queue

1. What is the runtime complexity of `enqueue` using a list?
    This should be a constant time O(n). Since you are just adding to the end of the list.

2. What is the runtime complexity of `enqueue` using a linked list?
    This should be a constant time O(1). Since you are just adding to the end of the list.

3. What is the runtime complexity of `dequeue` using a list?
    This should be a constant time O(n). Since you are just removing from the beginning of the list.

4. What is the runtime complexity of `dequeue` using a linked list?
    This should be a constant time O(n). Since you are just removing from the beginning of the list.

5. What is the runtime complexity of `len` using a list?
    The run time complexity of checking the len is linear time because it has to count each piece of the list.

6. What is the runtime complexity of `len` using a linked list?
    The run time complexity of checking the len is linear time because it has to count each piece of the list

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

## Binary Search Tree

1. What is the runtime complexity of `insert`?

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`?

4. What is the runtime complexity of `for_each`?

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
