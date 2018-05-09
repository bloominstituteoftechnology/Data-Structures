# Data Structures

https://gist.github.com/seanchen1991/05958a6c95994ad4db5c3070b7e9dfea
Topics:

* Linked Lists
* Queues
* Doubly Linked Lists
* Binary Search Trees
* Heaps

### Linked Lists

* Should have the methods: `addToTail`, `removeHead`, `contains`, and `getMax`.
  * `addToTail` replaces the tail with a new value that is passed in.
  * `removeHead` removes and returns the head node.
  * `contains` should search through the linked list and return true if a matching value is found.
  * `getMax` returns the maximum value in the linked list.
* The `head` property is a reference to the first node and the `tail` property is a reference to the last node. Build your nodes with objects.

![Image of Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/816px-Singly-linked-list.svg.png)

### Queues

* Should have the methods: `enqueue`, `dequeue`, `isEmpty` and a `length` getter.
  * `enqueue` should add an item to the back of the queue.
  * `dequeue` should remove and return an item from the front of the queue.
  * `isEmpty` should return `true` if the queue contains no elements, `false` otherwise.
  * A `length` getter that returns the number of items in the queue.

![Image of Queue](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/600px-Data_Queue.svg.png)

### Doubly Linked Lists

* Consists of a `DoublyLinkedList` class and a `ListNode` class.
* The `ListNode` class has the methods `insertAfter`, `insertBefore`, and `delete`.

  * `insertAfter` inserts a new node with the input value _after_ the calling node.
  * `insertBefore` inserts a new node with the input value _before_ the calling node.
  * `delete` should remove the calling node from the list (think about what that means).

* The `DoublyLinkedList` class, like the `LinkedList` class, holds references to the `head` of the list as well as the `tail`; it has the methods `addToHead`, `removeFromHead`, `addToTail`, `removeFromTail`, `moveToFront`, `moveToBack`, and `delete`
  * `addToHead` creates a new node with the input value and adds the new node as the new head of the list.
  * `addToTail` creates a new node with the input value and adds the new node as the new tail of the list.
  * `removeFromHead` removes the current head of the list; the current head's next node should be designated as the new head.
  * `removeFromTail` removes the current tail of the list; the current tail's previous node should be designated as the new tail.
  * `moveToFront` receives a node and moves that node (if it exists in the list) to the front of the list as the new head.
  * `moveToBack`receives a node and moves that node (if it exists in the list) to the back of the list as the new tail.
  * `delete` receives a node as input and deletes that node from the list.

![Image of Doubly Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)

### Binary Search Trees

* Should have the methods `insert`, `contains`, `getMax`, `depthFirstForEach`, and `breadthFirstForEach`.
  * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
  * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
  * `getMax` returns the maximum value in the binary search tree.
  * `depthFirstForEach` should iterate over the binary search tree in [depth-first](https://en.wikipedia.org/wiki/Depth-first_search) order, applying the supplied callback function to each tree element in turn.
  * `breadthFirstForEach` should iterate over the binary search tree in [breadth-first](https://en.wikipedia.org/wiki/Breadth-first_search) order, applying the supplied callback function to each tree element in turn.

![Image of Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png)

### Heaps

* Should have the methods `insert`, `delete`, `getMax`, `bubbleUp`, and `siftDown`.
  * `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
  * `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed.
  * `getMax` returns the maximum value in the heap _in constant time_.
  * `bubbleUp` moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
  * `siftDown` grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.
    ![Image of a Heap in Tree form](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Max-Heap.svg/501px-Max-Heap.svg.png)

![Image of a Heap in Array form](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Heap-as-array.svg/603px-Heap-as-array.svg.png)

## Tasks

1.  Set up your repository by running `npm install` in your root directory to install all necessary dependencies.

2.  Implement each data structure, starting with the linked list data structure. Run `npm test` to run the tests and check your progress. Get all the tests passing for each data structure.
