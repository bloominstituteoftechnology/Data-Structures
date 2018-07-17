For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1.  What is the runtime complexity of `add_to_tail`?
    O(1)

    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?
    O(n)

2.  What is the runtime complexity of `remove_head`?
    O(1)

3.  What is the runtime complexity of `contains`?
    O(n)

4.  What is the runtime complexity of `get_max`?
    O(n)

## Queue

1.  What is the runtime complexity of `enqueue`?
    O(1)

2)  What is the runtime complexity of `dequeue`?
    O(1)

3)  What is the runtime complexity of `len`?
    O(1)

## Binary Search Tree

1.  What is the runtime complexity of `insert`?
    operations | iterations ≈ log(n) => operation is almost equal tolog(n)
    O(log(n))

2.  What is the runtime complexity of `contains`?
    O(log(n))

3.  What is the runtime complexity of `get_max`?
    O(log(n))

## Heap

1.  What is the runtime complexity of `_bubble_up`?
    O(log(n))

2.  What is the runtime complexity of `_sift_down`?
    O(log(n))

3.  What is the runtime complexity of `insert`?
    O(log(n))

4.  What is the runtime complexity of `delete`?
    O(log(n))

5.  What is the runtime complexity of `get_max`?
    O(1)

## [Stretch Goal] Doubly Linked List

1.  What is the runtime complexity of `ListNode.insert_after`?
    O(1)

2.  What is the runtime complexity of `ListNode.insert_before`?
    O(1)

3.  What is the runtime complexity of `ListNode.delete`?
    O(1)

4.  What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    O(1)

5.  What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    O(1)

6.  What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    O(1)

7.  What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    O(1)

8.  What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    O(n) -> in general cases.
    O( n/2 ) half the time the general case -> implemented method

    - The implemented method goes in pararell form:
      - head to tail
      - tail to head
        When they reach or over pass each other the loop ends.

9.  What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    O(n) -> in general cases.
    O( n/2 ) half the time the general case -> implemented method

    - The implemented method goes in pararell form:
      - head to tail
      - tail to head
        When they reach or over pass each other the loop ends.

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

## [Stretch Goal] Doubly Linked List

1.  What is the runtime complexity of `ListNode.insert_after`? **O(1)**

2.  What is the runtime complexity of `ListNode.insert_before`? **O(1)**

3.  What is the runtime complexity of `ListNode.delete`? **O(1)**

4.  What is the runtime complexity of `DoublyLinkedList.add_to_head`? **O(1)**

5.  What is the runtime complexity of `DoublyLinkedList.remove_from_head`? **O(1)**

6.  What is the runtime complexity of `DoublyLinkedList.add_to_tail`? **O(1)**

7.  What is the runtime complexity of `DoublyLinkedList.remove_from_tail`? **O(1)**

8.  What is the runtime complexity of `DoublyLinkedList.move_to_front`? **O(1/2n)**

    - since we are using a front + a tail pointer we are coming out @ O(1/2n)
    - if you were to use only pointer we'd be at O(n)

9.  What is the runtime complexity of `DoublyLinkedList.move_to_end`? **O(1/2n)**

    - since we are using a front + a tail pointer we are coming out @ O(1/2n)
    - if you were to use only pointer we'd be at O(n)

10. What is the runtime complexity of `DoublyLinkedList.delete`? **O(1)**

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    `DoublyLinkedList.delete`

    - worst case complexity for array.splice should be O(n) as it creates a shadow copy of the indexes of the array it iterates over
    - deleting in our DDL should be constant time
