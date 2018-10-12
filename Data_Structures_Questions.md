For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `add_to_tail`?
    — Effectively, O(1) upon assessing value of Node(value). Seems that n would be value in that case from what I understand.

    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?
        — Then, we would need to add tail as another parameter in the method, so I think that it would be something more like O(n+m) where m is the tail and n is the value. But, that effectively reduces to O(n).

2. What is the runtime complexity of `remove_head`?
    — This is essentially a delete, but it holds the information of the previous node (a constant) and then it will point to the next node after what is to be deleted. So, this is still O(n) at worst, if it continues until the last node (effectively traversing each of the nodes).

3. What is the runtime complexity of `contains`?
    — This is essentially a search, so it checks the head of each node, and if the node holds that data, then it returns the node holding the requested data. Otherwise, it gets to the else/end and returns false. This makes it O(n) because of it visiting each node (at worst; it could reach the very last node and return the requested value— at best, it could find the value as early as O(1) if the requested value is at the beginning).

4. What is the runtime complexity of `get_max`?
    — The time complexity of 'get_max' is O(n) because each time the method is called, at worst, it will always visit every node in the list but only interact with them once to then determine what the max_value is, so n*1 operations.

## Queue

1. What is the runtime complexity of `enqueue`?
    — O(1) (should handle the item that's being added to the end, not checking other nodes)

2. What is the runtime complexity of `dequeue`?
    — O(1) (same as above, just starting with the front to find one node)

3. What is the runtime complexity of `len`?
    — O(1) (should just be retrieving a stored variable)


## Binary Search Tree

1. What is the runtime complexity of `insert`? 
    — 

2. What is the runtime complexity of `contains`?
    — 

3. What is the runtime complexity of `get_max`? 
    — 


## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## [Stretch Goal] Doubly Linked List

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