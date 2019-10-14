# Data Structures FAQ
## Contents
### General

#### My imports aren't working, help!
Python can be tricky with how imports work and can vary from environment to environment.  If you are having trouble, the easiest solution is to copy the file you want to import into the same folder as the file you want to import it into and use `from file import class`.

This is not a best practice for a real application, but it is acceptable for this exercise.  Just remember that this may mean if you want to change or update your code, you will have to do it in multiple places.

#### What are real-world use-cases for a Queue data structure?
Queues are used anywhere in which you want to work with data `First in First Out` (FIFO).  Server requests, without any prioritization, are handled this way. We'll also use it to conduct a breadth first traversal and breadth first search. 

#### What are real-world use-cases for a Stack data structure?
Stacks are used when you want to work with data `Last in First Out` (LIFO or FILO).  They're used in processor architecture,  undo logic, and depth first searches and traversals.

#### What are real-world use-cases for a Linked List data structure?
Linked Lists can be used to create `queues` and `stacks`.  They're also a key part of resolving collisions in hash tables, which we'll learn more about in a few weeks.

#### How are Linked-Lists different than an Array?
Both linked lists and arrays are linear data structures.  An array is the most space efficient type of storage possible and has great time complexity for most operations.  Logically, the array is linear in structure, and it is stored in a linear segment of memory.  It is accessed by starting at the memory address of the pointer and counting forward the number of bits resulting from the `index` times the size of the data type.  One weakness is the time complexity of operations that take data out of anywhere but the end and another is changing the size of the array.

A linked list is not as efficient for storage because each element requires a pointer to the next, and in a doubly-linked list, previous element.  It is also more difficult to access the elements.  Because there's no index, you must loop through the list to search for the item you want, which is O(n).  However, a linked list does not require a contiguous block of memory.  It has 0(1) to remove or add items anywhere in the list.

Generally speaking, it's usually best to use an array unless you expect to frequently add and remove items from anywhere other than the end.  In that case, it's better to use a linked list.  

#### I've always been able to add as much as I want to an Array and take things out from the beginning, end, or anywhere else.  It's never been a problem before, why are we bothering with all of this?
We're looking under the hood!  High level languages like Python abstract away most of the inner workings of everything we do.  Most of the time this is a good thing and most of the time it doesn't matter.  However, we're professional engineers and sometimes we need to solve problems where the details can have a major impact on success or failure.  Think about your car.  Do you know exactly how much weight you can put in it?  Probably not, nor do you need to.  But if you find yourself needing to put a load of bags of concrete in the trunk it suddenly becomes very important.  As an engineer, you'll be expected to understand when the details do and do not matter.

#### What are real-world use-cases for a LRU Cache?
An LRU cache is an efficient type of caching system that keeps recently used items and when the cache becomes full, pushes out the least recently used item in the cache.  It can be used any time a subset of data is used frequently that needs to be pulled from a source with a long lookup time.  For example, cacheing the most frequently accessed items from a database on a remote server.

#### What is the dictionary being used for in the LRU Cache?
We can't access items in a linked list directly because linked lists are not indexed.  To see if an item is already in the cache, we'd need to loop through the cache at O(n).  By also adding a dictionary to organize the nodes that are already present in memory, we index the linked list for a very small overhead cost.

#### What are real-world use-cases for a Binary Search Tree data structure?
A BST in the way that is being implemented for this Sprint is a bit too simple to see any real-world use-cases. There are many (more complex) variants of BSTs that do see production use. One very notable variant is the [B-tree](https://en.wikipedia.org/wiki/B-tree), which is a self-balancing ordered variant of the BST. B-trees play a critical role in database and file system indexing. Other notable variants include the AVL tree, which is a self-balancing BST and the prefix tree, which is specialized for handling text.

#### How is the root element of a Binary Search Tree decided?
The first element added to a BST is the root of the tree. However, doing it this way means that it's a very simple matter to end up with a lopsided BST. If we simply insert a monotonically ascending or descending sequence of values, then the tree would essentially flatten down to a linked list, and we'd lose all the benefits that a BST is supposed to confer. Self-balancing variants of the BST exist in order to alleviate this exact problem. 

#### What is the difference between Breadth First and Depth First?
In depth first, we pick one path at each branch and keep going forward until we hit a dead end, then  backtrack and take the first branch we find.  In breadth first, we go by layers, one row deeper each time.  This means that we jump around a bit.

#### What is the difference between a Search and a Traversal?
A search and a traversal are processed exactly the same.  The difference is that we stop a search when we find what we were looking for, or when all nodes have been visited without finding it.  In a traversal, we always keep going until we've visited every node.

