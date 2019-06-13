Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. Whruntime complexityat is the runtime complexity of `enqueue`?
O(1)


2. What is the runtime complexity of `dequeue`?
O(1)

3. What is the runtime complexity of `len`?
depending on implimentation of python len(list) could be anything between O(n) and O(1) where the implimentation mantains a current length

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
O(log n)

2. What is the runtime complexity of `contains`?
O(log n)

3. What is the runtime complexity of `get_max`? 
O(log n)

## Heap

1. What is the runtime complexity of `_bubble_up`?
for my _bubble up O(1)

2. What is the runtime complexity of `_sift_down`?
for my _sift_down O(log n)

3. What is the runtime complexity of `insert`?
O(log n)

4. What is the runtime complexity of `delete`?
O(log n)

5. What is the runtime complexity of `get_max`?
O(log n)

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

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?   The double linked list only needs to change some pointers in O(1), for the JavaScript Array.splice the worst-case would be having to allocate memory and move to it.   To find the index the array would likely be much faster for an unsorted array even though the search is O(n) for both array and double linked list.  A sorted array could have search O(log n).   A sorted double linked list search would still have search O(n).