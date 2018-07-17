For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

I refer to the base 2 logarithm by default when I write "log" below.

## Linked List

1. What is the runtime complexity of `add_to_tail`?

__O(1)__, since we have a pointer to the tail node.
  
    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?
    __O(n)__, since we would first need to find the tail node by starting at the head and repeatedly calling `get_next`.

2. What is the runtime complexity of `remove_head`?
__O(1)__

3. What is the runtime complexity of `contains`?
__O(n)__, since in the worst case we look at every node's value once.

4. What is the runtime complexity of `get_max`?
__O(n)__

## Queue

1. What is the runtime complexity of `enqueue`?
__O(1)__, since the storage is implemented in a Linked List, which has constant runtime complexity for its `add_to_tail` method.

2. What is the runtime complexity of `dequeue`?
__O(1)__

3. What is the runtime complexity of `len`?
__O(1)__, since there is a pointer directly to this.

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
__O(log(n))__, since we traverse the depth (d) of the tree, and the total nodes are equal to 2^d

2. What is the runtime complexity of `contains`?
__O(log(n))__

3. What is the runtime complexity of `get_max`? 
__O(log(n))__

## Heap

1. What is the runtime complexity of `_bubble_up`?
__O(log(n))__, since in the worst case one swap at every level of the implicit binary "tree" will be made

2. What is the runtime complexity of `_sift_down`?
__O(log(n))__

3. What is the runtime complexity of `insert`?
__O(log(n))__, since `_bubble_up` is called.

4. What is the runtime complexity of `delete`?
__O(log(n))__, since `_sift_down` is called.

5. What is the runtime complexity of `get_max`?
__O(1)__, since by the heap property, the max value will be the root node.

## [Stretch Goal] Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
__O(1)__

2. What is the runtime complexity of `ListNode.insert_before`?
__O(1)__

3. What is the runtime complexity of `ListNode.delete`?
__O(1)__

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
__O(1)__, since it calls `ListNode.insert_before` just once.

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
__O(1)__

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
__O(1)__

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
__O(1)__

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
__O(n)__, since it has to check if the node exists in the list.

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
__O(n)__

10. What is the runtime complexity of `DoublyLinkedList.delete`?
__O(1)__

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    `Array.splice` has to make copies of array elements, making it __O(n)__. So a doubly linked list has asymptotically better performance.