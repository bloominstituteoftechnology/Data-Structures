# Data Structures 

Topics:

 * Linked Lists
 * Queues
 * Binary Search Trees
 * Heaps

## Tasks
1. Implement each data structure, starting with the linked list data structure. Make sure you're in the approriate directory, then run `python3 test_[NAME OF DATA STRUCTURE].py` to run the tests for that data structure and check your progress. Get all the tests passing for each data structure.

2. Open up the `Data_Structures_Questions.md` file, which asks you to evaluate the runtime complexity of each of the methods you implemented for each data structure. Add your answers to each of the questions in the file.

### Linked Lists
 * Should have the methods: `add_to_tail`, `remove_head`, `contains`, and `get_max`.
   * `add_to_tail` replaces the tail with a new value that is passed in.
   * `remove_head` removes and returns the head node.
   * `contains` should search through the linked list and return true if a matching value is found.
   * `get_max` returns the maximum value in the linked list. 
 * The `head` property is a reference to the first node and the `tail` property is a reference to the last node. Build your nodes with objects.
 
![Image of Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/816px-Singly-linked-list.svg.png)

### Queues
 * Should have the methods: `enqueue`, `dequeue`, and `len`.
   * `enqueue` should add an item to the back of the queue.
   * `dequeue` should remove and return an item from the front of the queue.
   * `len` returns the number of items in the queue.
 
![Image of Queue](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/600px-Data_Queue.svg.png)

### Binary Search Trees
* Should have the methods `insert`, `contains`, `get_max`.
  * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
  * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
  * `get_max` returns the maximum value in the binary search tree.

![Image of Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png)

### Heaps
* Should have the methods `insert`, `delete`, `get_max`, `_bubble_up`, and `_sift_down`.
  * `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
  * `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed. 
  * `get_max` returns the maximum value in the heap _in constant time_.
  * `_bubble_up` moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
  * `_sift_down` grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.

![Image of a Heap in Tree form](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Max-Heap.svg/501px-Max-Heap.svg.png)

![Image of a Heap in Array form](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Heap-as-array.svg/603px-Heap-as-array.svg.png)

## Stretch Goals
1. Implement a [doubly-linked list](https://en.wikipedia.org/wiki/Doubly_linked_list) class that adheres to the following specification. Uncomment the tests in the `tests/doubly-linked-list.test.js` file in order to test your solution.

   * Consists of a `DoublyLinkedList` class and a `ListNode` class.
   * The `ListNode` class has the methods `insert_after`, `insert_before`, and `delete`.
     * `insert_after` inserts a new node with the input value _after_ the calling node.
     * `insert_before` inserts a new node with the input value _before_ the calling node.
     * `delete` should remove the calling node from the list (think about what that means).

   * The `DoublyLinkedList` class, like the `LinkedList` class, holds references to the `head` of the list as well as the `tail`; it has the methods `add_to_head`, `remove_from_head`, `add_to_tail`, `remove_from_tail`, `move_to_front`, `move_to_back`, and `delete`
     * `add_to_head` creates a new node with the input value and adds the new node as the new head of the list.
     * `add_to_tail` creates a new node with the input value and adds the new node as the new tail of the list.
     * `remove_from_head` removes the current head of the list; the current head's next node should be designated as the new head.
     * `remove_from_tail` removes the current tail of the list; the current tail's previous node should be designated as the new tail.
     * `move_to_front` receives a node and moves that node (if it exists in the list) to the front of the list as the new head.
     * `move_to_end`receives a node and moves that node (if it exists in the list) to the back of the list as the new tail.
     * `delete` receives a node as input and deletes that node from the list.

![Image of Doubly Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)