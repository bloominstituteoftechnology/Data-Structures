# Data Structures

* like cookware. data structures are the cookware
    - pot for noodles
        * functions for noodles
    - pot for sauce
        * functions for sauce, but very similar to above
    - colander to drain pasta
        * another function completely

when you use data structures, you store data inside them. Just like if you're cooking, the cookware is storing your food. It's not the final spot, but an intermediate storage place to store stuff (data/food)

the cookware transforms the food to a different form in the same way that data structures transform data.

data structures have a storage characteristic in common even though their function might be different. 

Data Structure = **Intermediate Storage Place!**

Algorithims are not data structure. Data structures are the tools and algorithim is the recipe you follow.

arrays are lists and objects are dictionaries in Python. 

---------

TODO: implement data structures listed in repo

in order to implement, we need to have a conceptual understanding of what each of the data structures do. 

---------
## Linked Lists
* alternative to arrays or lists

* used for the same types of things an array or reg list is used for:
    to store things!
* fundamental difference betweeb list/array and a linked-list, is that arrays/list have memory earmarked up front. More expensive as far as time/complexity goes
* a linked list uses memory only as needed. Empty linked lists take no memory at all. Linked lists don't require for you to know how much memory you need up front. 

----------
## Nodes
* nothing more than a dictionary/object or class that holds a value and a next:

        Node{
            value: some.value
            next: next_node
        }

## Queue
* encapsulates the functionality of a line(or queue)
    * First In, First Out(FIFO)
        - not to be confused with LIFO (last in, first out --- characteristic of a Stack)

# Binary Search Tree
* has at most two children per node
* has a left and a right property
    - right: greater than or equal to
    - left: less than
* enables faster searching because we are basically splitting the data into two.  

# Heap
* most efficient out of all the data structures
* heap always tries to haven the max value at the top of the heap. The rest of the values will have some sort of ordering that's efficient. 

* Ordering rules: children have to be less than direct parent.

* heap swapping:
    - new value inserted at the bottom of the heap
    - check parent. If less than child...SWAP!
    - do until the new node is greater than its child. 
    - this is called bubbling up.
    













