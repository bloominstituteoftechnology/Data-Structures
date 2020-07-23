# Module 1 - Data Structure

Constant Time: Runtime Complexity - Big O notation = O(constant) or O(1) = An objective way to "measure" the efficiency of code/algorithms Constant Time: An Operation that takes the same amount of time regardless of input size. (i.e commands[1] or commands[99] takes the same amount of time tie run, accessing a dictionary value by key)

Linear Time Big O notation = O(n) or O(constant * n): An operation that DOES depend on the size of the input;
the time the operation takes increases linearlywith the input size. (i.e for loops of lists or dicts. # Linear time operation)

Quadratic time - Big O notation = O (m * n) or O(n^2): An operation that DOES depend on the size of the input; the time operation takes increases quadratically with the input size. (i.e enumerating all possible pairs from two lists[nested for loop],
length of list one multiplied by length of list 2)

Big O says we get to toss out constant values.

## Linked List

### Compare and contrast linked lists vs. arrays(Python lists)

Array - [1, 2, 3, 4, 5, 6, 7] contiguous - all of theses are layed out next to each other.

Linked list - Each value is contained inside of its own node. (i.e node1 ---> node2---> node3)

class Node:

    value
    next
O(n): Before we added 'tail' we had to start from the head and traverse all the way to the end of the linked list to add a new element.

We added a 'tail': Add a new element onto the end of a linked list
O(1): 1. Create the new node from the value
      2. Set the old tail's next to point to the new node
      3. Reassign self.tail to refer to the new node

Stacks: Stack of Plates  add to top of stack and remove from top of stack as well.

Last in First Out = Stacks exhibit this property

Queues: Grocery Line - Enter on one end and Leave on the other end

First in First Out Ordering
