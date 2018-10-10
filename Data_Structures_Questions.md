For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `add_to_tail`?
  
    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?

2. What is the runtime complexity of `remove_head`?

3. What is the runtime complexity of `contains`?

4. What is the runtime complexity of `get_max`?

#### Answers

1. `add_to_tail` has a runtime of O(1), because we have a reference to our tail.
     
     a. If we didn't have a pointer to our tail, the operation itself costs O(1), but we would have to traverse to the tail, which would cost O(n).

2. `remove_head` has a runtime complexity of O(1).

3. `contains` has a worst case runtime complexity of O(n) e.g. when not in list.

4. `get_max` has a run time complexity of O(n), because we have to traverse all nodes to get the max. We could do something similar to the max_stack we implemented earlier, to trade space complexity for a get_max runtime of O(1), since we have reference to the tail.
## Queue

1. What is the runtime complexity of `enqueue`?

2. What is the runtime complexity of `dequeue`?

3. What is the runtime complexity of `len`?

#### Answers

1. `enqueue` has a runtime complexity of O(1). This is possible due to us having a pointer to the tail in our linked list.

2. `dequeue` has a runtime complexity of O(1).

3. `len` has a run time complexity of O(1), because we're using memory to keep track of the size.

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

#### Answers

1. `insert` has an average runtime complexity of O(log n). However, there can be a bad implemented tree, which can cause a worst case O(n) time complexity.

2. `contains` follows the same reasoning as insert, average O(log n), worst case O(n)

3. `get_max` also follows the same reasoning, average O(log n), worst case O(n) e.g. when root is min of whole tree, and nodes only have children on the right

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