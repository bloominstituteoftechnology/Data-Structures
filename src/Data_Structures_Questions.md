For each of the methods associated with each data structure, classify it based on its runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `addToTail`?
  O(1)
    a. What if our list implementation didn't have a reference 
    to the tail of the list in its constructor? What would be the runtime of the `addToTail` method?
O(n)

2. What is the runtime complexity of `removeHead`?
O(n)

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
O(log(n))

2. What is the runtime complexity of `contains`?
O(log(n))
3. What is the runtime complexity of `getMax`? 
O(log(n))
## Heap

1. What is the runtime complexity of `bubbleUp`?
O(nlog(n))
2. What is the runtime complexity of `siftDown`?
O(log(n))
3. What is the runtime complexity of `insert`?
O(log(n))
4. What is the runtime complexity of `delete`?
O(log(n))
5. What is the runtime complexity of `getMax`?
O(log(n))
## [Stretch Goal] Doubly Linked List

1. What is the runtime complexity of `ListNode.insertAfter`?

2. What is the runtime complexity of `ListNode.insertBefore`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.addToHead`?

5. What is the runtime complexity of `DoublyLinkedList.removeFromHead`?

6. What is the runtime complexity of `DoublyLinkedList.addToTail`?

7. What is the runtime complexity of `DoublyLinkedList.removeFromTail`?

8. What is the runtime complexity of `DoublyLinkedList.moveToFront`?

9. What is the runtime complexity of `DoublyLinkedList.moveToBack`?

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the `Array.splice` method. Which method generally performs better?