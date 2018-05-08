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
    if (value > this.value) {
      if (!this.right) this.right = new BinarySearchTree(value);
      else this.right.insert(value)
    } else {
      if (!this.left) this.left = new BinarySearchTree(value);
      else this.left.insert(value)
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    if (target > this.value) {
      if (this.right.value === target) return true;
      if (this.right.right === null && this.right.left === null) return false;
      else return this.right.contains(target);
    } else {
      if (this.left.value === target) return true;
      if (this.left.right === null && this.left.left === null) return false;
      else return this.left.contains(target);
    }
  }

  /* Returns the maximum this. in the tree 
  Should not remove the max value from the tree */
  getMax() {
    if (this.right === null && this.left === null) return this.value;
    else if (this.right) return this.right.getMax();
    else if (this.left.value > this.value) return this.left.getMax();
  }

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {
    cb(this.value);
    if (this.left) this.left.depthFirstForEach(cb);
    if (this.right) this.right.depthFirstForEach(cb);
  }

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {
    const queue = [];

    queue.push(this);

    while (queue.length > 0 ) {
      if (queue[0].left) queue.push(queue[0].left);
      if (queue[0].right) queue.push(queue[0].right);
      cb(queue[0].value)
      queue.shift();
    }
  }
}

module.exports = BinarySearchTree;