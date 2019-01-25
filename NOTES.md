sets no order
check with dir(s) venn diagram, subset
s = set()
s.add('val')
s.add('val2')
s
('val', 'val2') or ('val2', 'val') since it is unordered

insert(bst, val)
  if val = bst.val:
  return
  elif val < bst.val
    if null:
    create leaf
    
binary closer to merge sort vs quick sort?



Traversal
Breadth First [arr]
Depth First
        8
    3     10
1     6       14
    4   7    13

8 3 1 6 4 7 10 14 13
831
6 4 7
10 14 13

Pre-order
In order
Post-order

  def print_tree(self):
    if self.left is not None:
      self.left.print_tree()
    print(self.value)
    if self.right is not None:
      self.right.print_tree()

# DEPTH FIRST SEARCH
Pre Order
F B A D C E G I H
In Order
A B C D E F G H I
Post-Order
A C E D B H I G F

        F
    B     G
A     D       I
    C   E    H

# BREADTH FIRST SEARCH
Use a queue to keep values



def bft(self):
  queue = Queue()
  visited = []

Depth first change queue to a stack !!!!!

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

stack = []

visited = []  [A, C, F, E, B, D, B]

vertex = A => C => F => E => B => D 

