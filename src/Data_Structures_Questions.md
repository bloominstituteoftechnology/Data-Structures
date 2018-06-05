For each of the methods associated with each data structure, classify it based on its runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `addToTail`?
O(1)  
    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `addToTail` method?

2. What is the runtime complexity of `removeHead`?
O(1)

3. What is the runtime complexity of `contains`?
O(n)

4. What is the runtime complexity of `getMax`?
O(n)

## Queue

1. What is the runtime complexity of `enqueue`?
O(1)

2. What is the runtime complexity of `dequeue`?
O(1)

3. What is the runtime complexity of `isEmpty`?
O(1)

4. What is the runtime complexity of `length`?
O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`?
O(logn) 

2. What is the runtime complexity of `contains`?
O(logn)

3. What is the runtime complexity of `getMax`? 
O(logn)

## Heap

1. What is the runtime complexity of `bubbleUp`?
O(logn)

2. What is the runtime complexity of `siftDown`?
O(logn)

3. What is the runtime complexity of `insert`?
O(logn)

4. What is the runtime complexity of `delete`?
O(logn)

5. What is the runtime complexity of `getMax`?
O(1)

## [Stretch Goal] Doubly Linked List

1. What is the runtime complexity of `ListNode.insertAfter`?
O(1)

2. What is the runtime complexity of `ListNode.insertBefore`?
O(1)

3. What is the runtime complexity of `ListNode.delete`?
O(1)

4. What is the runtime complexity of `DoublyLinkedList.addToHead`?
O(1)

5. What is the runtime complexity of `DoublyLinkedList.removeFromHead`?
O(1)

6. What is the runtime complexity of `DoublyLinkedList.addToTail`?
O(1)

7. What is the runtime complexity of `DoublyLinkedList.removeFromTail`?
O(1)

8. What is the runtime complexity of `DoublyLinkedList.moveToFront`?
O(1) or O(n) depending on implementation

9. What is the runtime complexity of `DoublyLinkedList.moveToBack`?
O(1) or O(n) depending on implementation

10. What is the runtime complexity of `DoublyLinkedList.delete`?
O(1)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the `Array.splice` method. Which method generally performs better?