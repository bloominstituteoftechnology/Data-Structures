# Data Structures

Topics:

- Singly Linked Lists
- Queues and Stacks
- Doubly Linked Lists
- Binary Search Trees
- Related Code Challenge Problems

Stretch Goals:

- LRU Cache
- Heaps
- AVL Trees

## Completion Requirements

- Module 1: Implement the Stack and Queue classes using built-in Python lists and the Node and LinkedList classes you created during the Module 1 Guided Project.
- Module 2: Implement the Doubly Linked List class
- Module 3: Implement the Binary Search Tree class
- Module 4: Implement traversal methods on Binary Search Trees

> NOTE: The quickest and easiest way to reliably import a file in Python is to just copy and paste the file you want to import into the same directory as the file that wants to import. This obviously isn't considered best practice, but it is the most reliable way to do it across all platforms. If the import isn't working, feel free to try this method.

### Stacks

- Should have the methods: `push`, `pop`, and `len`.
  - `push` adds an item to the top of the stack.
  - `pop` removes and returns the element at the top of the stack
  - `len` returns the number of elements in the stack.

### Queues

- Has the methods: `enqueue`, `dequeue`, and `len`.
  - `enqueue` adds an element to the back of the queue.
  - `dequeue` removes and returns the element at the front of the queue.
  - `len` returns the number of elements in the queue.

![Image of Queue](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/600px-Data_Queue.svg.png)

### Doubly Linked Lists

- The `ListNode` class, which represents a single node in the doubly-linked list, has already been implemented for you. Inspect this code and try to understand what it is doing to the best of your ability.
- The `DoublyLinkedList` class itself should have the methods: `add_to_head`, `add_to_tail`, `remove_from_head`, `remove_from_tail`, `move_to_front`, `move_to_end`, `delete`, and `get_max`.
  - `add_to_head` replaces the head of the list with a new value that is passed in.
  - `add_to_tail` replaces the tail of the list with a new value that is passed in.
  - `remove_from_head` removes the head node and returns the value stored in it.
  - `remove_from_tail` removes the tail node and returns the value stored in it.
  - `move_to_front` takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down.
  - `move_to_end` takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up.
  - `delete` takes a reference to a node in the list and removes it from the list. The deleted node's `previous` and `next` pointers should point to each afterwards.
  - `get_max` returns the maximum value in the list.
- The `head` property is a reference to the first node and the `tail` property is a reference to the last node.

![Image of Doubly Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)

### Binary Search Trees

- Should have the methods `insert`, `contains`, `get_max`.
  - `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
  - `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
  - `get_max` returns the maximum value in the binary search tree.
  - `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work.

![Image of Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png)

---

Once you've gotten the tests passing, it's time to analyze the runtime complexity of your `get` and `set` operations. There's a way to get both operations down to sub-linear time. In fact, we can get them each down to constant time by picking the right data structures to use.

Here are you some things to think about with regards to optimizing your implementation: If you opted to use a dictionary to work with key-value pairs, we know that dictionaries give us constant access time, which is great. It's cheap and efficient to fetch pairs. A problem arises though from the fact that dictionaries don't have any way of remembering the order in which key-value pairs are added. But we definitely need something to remember the order in which pairs are added. Can you think of some ways to get around this constraint?

## Stretch Goals

### LRU Cache

An LRU (Least Recently Used) cache is an in-memory storage structure that adheres to the [Least Recently Used](<https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)>) caching strategy.

In essence, you can think of an LRU cache as a data structure that keeps track of the order in which elements (which take the form of key-value pairs) it holds are added and updated. The cache also has a max number of entries it can hold. This is important because once the cache is holding the max number of entries, if a new entry is to be inserted, another pre-existing entry needs to be evicted from the cache. Because the cache is using a least-recently used strategy, the oldest entry (the one that was added/updated the longest time ago) is removed to make space for the new entry.

So what operations will we need on our cache? We'll certainly need some sort of `set` operation to add key-value pairs to the cache. Newly-set pairs will get moved up the priority order such that every other pair in the cache is now one spot lower in the priority order that the cache maintains. The lowest-priority pair will get removed from the cache if the cache is already at its maximal capacity. Additionally, in the case that the key already exists in the cache, we simply want to overwrite the old value associated with the key with the newly-specified value.

We'll also need a `get` operation that fetches a value given a key. When a key-value pair is fetched from the cache, we'll go through the same priority-increase dance that also happens when a new pair is added to the cache.

Note that the only way for entries to be removed from the cache is when one needs to be evicted to make room for a new one. Thus, there is no explicit `remove` method.

Given the above spec, try to get a working implementation that passes the tests. What data structure(s) might be good candidates with which to build our cache on top of? Hint: Since our cache is going to be storing key-value pairs, we might want to use a structure that is adept at handling those.

### AVL Tree

An AVL tree (Georgy Adelson-Velsky and Landis' tree, named after the inventors) is a self-balancing binary search tree. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property.

We define balance factor for each node as :

```
balanceFactor = height(left subtree) - height(right subtree)
```

The balance factor of any node of an AVL tree is in the integer range [-1,+1]. If after any modification in the tree, the balance factor becomes less than −1 or greater than +1, the subtree rooted at this node is unbalanced, and a rotation is needed.

![AVL tree rebalancing](https://s3.amazonaws.com/hr-challenge-images/0/1436854305-b167cc766c-AVL_Tree_Rebalancing.svg.png)

Implement an AVL Tree class that exhibits the aforementioned behavior. The tree's `insert` method should perform the same logic as what was implemented for the binary search tree, with the caveat that upon inserting a new element into the tree, it will then check to see if the tree needs to be rebalanced.

How does the time complexity of the AVL Tree's insertion method differ from the binary search tree's?
