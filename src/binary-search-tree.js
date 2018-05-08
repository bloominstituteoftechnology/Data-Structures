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
    if (value < this.value) {
      if (this.left === null) {
        this.left = new BinarySearchTree(value);
      }else {
        this.left.insert(value);
      }
    }else if (value > this.value) {
      if (this.right === null) {
        this.right = new BinarySearchTree(value);
      }else {
        this.right.insert(value);
      }
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    if (target === this.value) return true;
    if (this.value > target && this.left) return this.left.contains(target);
    if (this.value < target && this.right) return this.right.contains(target);
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    if (!this) return null;

    let max = this.value;
    let current = this;

    while(current) {
      if(current.value > max) {
        max = current.value;
      }
      current = current.right;
    }
    return max;
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
    let queue = [this];
    for (let i = 0; i < queue.length; i++) {
      let node = queue[i];
      if (node.left) {
        queue.push(node.left);
      }
      if (node.right) {
        queue.push(node.right);
      }
      cb(node.value);
    }
  }
}

module.exports = BinarySearchTree;