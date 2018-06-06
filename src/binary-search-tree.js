const Queue = require('./queue');

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
  insert(x) {
    if (x < this.value && this.left) {
      this.left.insert(x);
    }
    if (x < this.value && !this.left) {
      this.left = new BinarySearchTree(x)
    }
    if (x > this.value && this.right) {
      this.right.insert(x)
    }
    if (x > this.value && !this.right) {
      this.right = new BinarySearchTree(x)

    }


  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    if (this.value === target) {
      return true;
    }

    if (target < this.value) {
      if (this.left) {
        if (this.left.contains(target)) return true;
      }
    }
    else {
      if (this.right) {
        if (this.right.contains(target)) return true;
      }
    }
    return false;

  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    if (this.left === null && this.right === null) return this.value;

    else {
      if (this.right) return this.right.getMax();
      else return this.left.getMax();
    }
  }


  depthFirstForEach(cb) {
    // invoke the cb on the current node we're on
    cb(this.value);
    if (this.left) {
      this.left.depthFirstForEach(cb);
    }
    if (this.right) {
      this.right.depthFirstForEach(cb);
    }
  }

  breadthFirstForEach(cb) {
    // use a queue
    const q = new Queue();
    // push our root node onto our queue
    q.enqueue(this);
    // iterate through our queue until it is empty
    while (!q.isEmpty()) {
      // dequeue the next node in line
      const node = q.dequeue();
      // add the node's children to the queue if they exists
      if (node.left) q.enqueue(node.left);
      if (node.right) q.enqueue(node.right);
      cb(node.value);
    }
  }




}


module.exports = BinarySearchTree;



