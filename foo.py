# STRUCTURE A,B,C, none
        head      tail 
        v         v
None -  A -> B -> C - None
        ^    ^    ^
        p    q    r

head.next_node === B
head.next_node.next_node === C
head.next_node.next_node.next_node === None

tail.next_node === None

# change STRUCTURE into C,B,A none:
        C -> B -> A - None

# change pointers instead of changing objects/variables/data
    None - A <- B <- C

# its still C,B,A, none


