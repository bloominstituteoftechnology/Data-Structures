# Data Structures FAQ
## Contents
### General

#### What are real-world use-cases for a Queue data structure?
If there is high inflation and high taxes a retailer can reduce tax expense with LIFO.

#### What are real-world use-cases for a Linked List data structure?
A train that drops off and adds cars based on demand for the items in one of many cars and availability of cars with items at each stop where emptying a car is too 
time consuming compared to detaching the car.


#### What are real-world use-cases for a Binary Search Tree data structure?
A BST in the way that is being implemented for this Sprint is a bit too simple to see any real-world use-cases. There are many (more complex) variants of BSTs that do see production use. One very notable variant is the [B-tree](https://en.wikipedia.org/wiki/B-tree), which is a self-balancing ordered variant of the BST. B-trees play a critical role in database and file system indexing. Other notable variants include the AVL tree, which is a self-balancing BST and the prefix tree, which is specialized for handling text.

#### How is the root element of a Binary Search Tree decided?
The first element added to a BST is the root of the tree. However, doing it this way means that it's a very simple matter to end up with a lopsided BST. If we simply insert a monotonically ascending or descending sequence of values, then the tree would essentially flatten down to a linked list, and we'd lose all the benefits that a BST is supposed to confer. Self-balancing variants of the BST exist in order to alleviate this exact problem. 

#### What are real-world use-cases for a Heap data structure?
Print or concatenate in order a set of in order lists.   Getting the max or min of a set of dynamically changing values. For example ticketmaster keeping current min and max available prices as tickets are being sold online.

