Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
    For the way I implemented this data structure, the runtime complexity is O(1).


2. What is the runtime complexity of `dequeue`?

    The runtime comlexity is O(n) because whenever I pop the first element of the queue, all of the other elements need to shift over one space to the left to close the gap created by the element being removed from the araray.

3. What is the runtime complexity of `len`?
    This is O(n) because it is looping through each index to find the length of the array.


## Binary Search Tree

1. What is the runtime complexity of `insert`? 
    O(log n) because the algorithm needs to go through part of the tree, we are not iterating over all nodes, only some of them.

2. What is the runtime complexity of `contains`?
    In the best case scenario this is O(log n), but worst case this is O(n). It is O(n) because I would need to go through every node before I would be able to return false.

3. What is the runtime complexity of `get_max`? 
    This is O(log n) I'm only going down the rightmost nodes in the tree.


## Heap

1. What is the runtime complexity of `_bubble_up`?
    The runtime complexity is O(log n)

2. What is the runtime complexity of `_sift_down`?
    The runtime complexity is O(log n)

3. What is the runtime complexity of `insert`?
    The runtime complexity is  O(log n)

4. What is the runtime complexity of `delete`?
    The runtime complexity is  O(log n)
    
5. What is the runtime complexity of `get_max`?
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
        The JS `Array.splice` method has a worst-case runtime complexity O(n), because in the worst case you are copying nearly all of the elements of the array into a new array. For smaller data sets I would prefer using an array, just because of indexes and overall ease of use. However, with larger and larger data sets the DLL's `delete` method's superior performance would become more apparent.
