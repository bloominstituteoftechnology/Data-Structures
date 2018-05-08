class BinarySearchTree {
  /* Do not modify the constructor */
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  /* Inserts the given value
  Make sure the rules of a binary search
  tree are being adhered to */
  insert(value) {
    const newNode = new BinarySearchTree(value);
    if (value > this.value) {
      //insert right or below right
      if (!this.right) this.right = newNode;
      else this.right.insert(value);
    } else if (value < this.value) {
      //insert left or below left
      if (!this.left) this.left = newNode;
      else this.left.insert(value);
    } else {
      //value == this.value, dont add
      return null;
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    //check main node
    if (target === this.value) return true;
    if (target > this.value) {
      if (this.right) if (this.right.contains(target)) return true;
    } else {
      if (this.left) if (this.left.contains(target)) return true;
    }
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    if (this.value) {
      if (this.right) return this.right.getMax();
      else return this.value;
    }
  }

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {
    // first invoke on current node
    cb(this.value);
    if (this.left) this.left.depthFirstForEach(cb);
    if (this.right) this.right.depthFirstForEach(cb);
  }

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {
    //use a queue to get order of elements
    const q = [];
    //push root node into the queue
    q.push(this);
    //iterate through queue til empty
    while (q.length > 0) {
      //remove item from queue and work on it
      const node = q.shift();
      //add node children to node
      if (node.left) q.push(node.left);
      if (node.right) q.push(node.right);
      cb(node.value);
    }
  }
}

module.exports = BinarySearchTree;
