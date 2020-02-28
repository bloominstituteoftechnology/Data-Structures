Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
O(1) because items that enter the queue are in a set order

2. What is the runtime complexity of `dequeue`?
If the time complexity is normally O(1) because it is similar to an ordered list

3. What is the runtime complexity of `len`?
O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
O(n)

2. What is the runtime complexity of `contains`?
O(n)

3. What is the runtime complexity of `get_max`? 
O(n)

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

Insert/delete at head is O(1) since you already have the head.
Insert/delete at an arbitrary location is going to be O(n) since you are going to potentially have to traverse the entire list, O(n), to find the location to insert. There is an exception to this described below.
Insert/delete at the end (append) is going to be O(n) since you have to traverse the whole list to get to the end.
Lookup is going to be O(n) since you potentially have to traverse the entire list.

Now consider adding a tail tracker to the list. Most people would still consider this a “simple” linked list. By keeping track of the tail, append is now O(1). So if you compare a singly linked list with a tail tracker to a doubly linked list without, you will see a performance difference that is actually in favor of the singly-linked list. The performace difference has nothing to do with singleness or doubleness of the list. It’s a fairly common performance enhancement for any list where append performance is an issue.

Now consider the case where you already have the node of interest. Deleting it from a doubly linked list is going to be O(1) but O(n) for the singly linked list.

The core issue is that to update the list, you need to know the node before the location you want to manipulate. Manipulating the pointers themselves is a constant time operation so the real issue is how fast can you find that previous node. With that understanding, it should be fairly straightforward to figure out the performance of any given implementation.

1. What is the runtime complexity of `ListNode.insert_after`?
O(n)

2. What is the runtime complexity of `ListNode.insert_before`?
O(n)

3. What is the runtime complexity of `ListNode.delete`?
O(n)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(n)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(n)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(n)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

11. Search: 
O(n)

12. Access:
O(n)