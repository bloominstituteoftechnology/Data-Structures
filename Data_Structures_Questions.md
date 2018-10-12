For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `add_to_tail`?
  
  add to tail has complexity O(1) since only one operation is needed in order to insert a new value on the tail. 

    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?

    Without a reference to the tail, the complexity would become O(n) since each item in the list would be checked by the function in order to add the new tail. 

2. What is the runtime complexity of `remove_head`?

    Although there are several conditional cases in the function, I believe each of them is O(1) so the overal complexity would reduce to O(1).

3. What is the runtime complexity of `contains`?

    This function would have complexity O(n) since each item in the list needs to be checked making the number of elements equal to the number of operations. 

4. What is the runtime complexity of `get_max`?

    The get_max function also has O(n) complexity since it involves checking every item.

## Queue

1. What is the runtime complexity of `enqueue`?

    enqueue has complexity O(1) since only one operation is performed regarless of the number of elements in the list

2. What is the runtime complexity of `dequeue`?

    dequeue has complexity O(1) since only one operation is performed regarless of the number of elements in the list


3. What is the runtime complexity of `len`?

    the len function is only finding a stored value and therefore has complexity O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

    I believe that each of the functions in the binary search tree have complexity log(n).  This is because they all involve comparisons where after each comparision the number of remaining elements is reduced. 

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