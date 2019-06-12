# Construct a Linked List by Merging Alternate Nodes of Two Given Lists

Given two linked lists, merge their nodes together to make a single linked list.
This final linked list should take nodes from each of the two input linked lists
in alternating fashion, starting with the first linked list and then alternating
with the second linked list. If either linked list runs out of nodes as the
final linked list is being constructed, all of the nodes from the other linked
list should be concatenated onto the end of the final linked list. 

For example, given two linked lists
```
[A]->[B]->[C]->N

[1]->[2]->[3]->N
```

The final linked list would be 
```
[A]->[1]->[B]->[2]->[C]->[3]->N
```

Analyze the time and space complexity of your solution. 
