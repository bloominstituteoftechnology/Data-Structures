For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `add_to_tail`?
  
    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?

    The runtime complexity is O(1). 
    
    If the list didn't keep track of the tail, it would have to be looped over in order to get the last item, and the runtime complexity would be O(n)

2. What is the runtime complexity of `remove_head`?

    O(1)

3. What is the runtime complexity of `contains`?

    O(n)

4. What is the runtime complexity of `get_max`?

    O(n)

## Queue

1. What is the runtime complexity of `enqueue`?

    O(1)

2. What is the runtime complexity of `dequeue`?

    O(1)

3. What is the runtime complexity of `len`?

    O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

    O(log n)

2. What is the runtime complexity of `contains`?

    O(log n)

3. What is the runtime complexity of `get_max`? 

    O(log n)

## Heap

1. What is the runtime complexity of `_bubble_up`?

    O(log n)

2. What is the runtime complexity of `_sift_down`?

    O(log n)

3. What is the runtime complexity of `insert`?

    O(log n) ?(because it calls `_bubble_up`)

4. What is the runtime complexity of `delete`?

    O(log n) ?(because it calls `_sift_down`)

5. What is the runtime complexity of `get_max`?

    O(1)

## [Stretch Goal] Doubly Linked List

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

    O(n)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

    O(n)

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    O(1)

    I don't know what the worst-case runtime is for Array.splice.