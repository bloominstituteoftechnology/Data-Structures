Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list?
O(1)
2. What is the runtime complexity of `push` using a linked list?
O(1)
3. What is the runtime complexity of `pop` using a list?
O(1) assuming popping of the last element, otherwise it would be O(n)
4. What is the runtime complexity of `pop` using a linked list?
O(1) assuming we have a pointer to the last element, otherwise it would be O(n)
5. What is the runtime complexity of `len` using a list?
O(1)
6. What is the runtime complexity of `len` using a linked list?
O(1) 

## Queue

1. What is the runtime complexity of `enqueue` using a list?
O(1)
2. What is the runtime complexity of `enqueue` using a linked list?
O(1)
3. What is the runtime complexity of `dequeue` using a list?
O(n) because we have to shift each element over when dequeueing the first element
4. What is the runtime complexity of `dequeue` using a linked list?
O(1)
5. What is the runtime complexity of `len` using a list?
O(1)
6. What is the runtime complexity of `len` using a linked list?
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
    Haha, I have no idea about JS Array.splice, iOS student here... Could look it up, but not really wanting to right now

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
O(h) where h is the height of the tree
O(n) is worst case (unbalanced tree), assuming balanced tree: O(log(n)) on average
O(h) where h is the height of the tree
2. What is the runtime complexity of `contains`?
O(h) where h is the height of the tree
O(n) is worst case (unbalanced tree), assuming balanced tree: O(log(n)) on average
3. What is the runtime complexity of `get_max`? 
O(h) where h is the height of the tree
O(n) is worst case (unbalanced tree), assuming balanced tree: O(log(n)) on average
4. What is the runtime complexity of `for_each`?
O(n), you must iterate through each element

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
