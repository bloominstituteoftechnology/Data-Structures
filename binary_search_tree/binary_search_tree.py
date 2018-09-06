class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # Inserts the given value
  # Make sure the rules of a binary search
  # tree are being adhered to
  def insert(self, value):
    newNode = BinarySearchTree(value)
    
    if value > self.value:
      #insert right or below right
      if not self.right: self.right = newNode
      else: self.right.insert(value)
    elif value < self.value:
      #insert left or below left
      if not self.left: self.left = newNode
      else: self.left.insert(value)
    else:
      return None

# Traverses the tree until either the
#   target value has been found in the true
#   or the entire tree has been searched.
#   Returns true or false accordingly
  def contains(self, target):
    #check main node
    if target is self.value: return True
    if target > self.value:
      if self.right:
        if self.right.contains(target): return True
    else:
      if self.left:
        if self.left.contains(target): return True
    return False

# Returns the maximum value in the tree 
#   Should not remove the max value from the tree
  def get_max(self):
    if self.value:
      if self.right: return self.right.get_max()
      else: return self.value







  #  Traverses the tree in a 'vertical' fashion,
  # from parent to child. Executes the given callback
  # on each visited tree node 
  # depthFirstForEach(cb) {
  #   // first invoke on current node
  #   cb(this.value);
  #   if (this.left) this.left.depthFirstForEach(cb);
  #   if (this.right) this.right.depthFirstForEach(cb);
  # }

  #  Traverses the tree in a 'horizontal' fashion,
  # from sibling to sibling. Executes the given callback
  # on each visited tree node 
  # breadthFirstForEach(cb) {
  #   //use a queue to get order of elements
  #   const q = [];
  #   //push root node into the queue
  #   q.push(this);
  #   //iterate through queue til empty
  #   while (q.length > 0) {
  #     //remove item from queue and work on it
  #     const node = q.shift();
  #     //add node children to node
  #     if (node.left) q.push(node.left);
  #     if (node.right) q.push(node.right);
  #     cb(node.value);
  #   }
  # }