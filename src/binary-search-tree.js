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
        this.length++;
      } else {
        this.left.insert(value);
      }
    } else {
      if (this.right === null) {
        this.right = new BinarySearchTree(value);
        this.length++;
      } else {
        this.right.insert(value);
      }
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    if (target === this.value) {
      return true;
    } else {
      if (target < this.value) {
        if (this.left === null) {
          return false;
        }
        return this.left.contains(target);
      } else {
        if (this.right === null) {
          return false;
        }
        return this.right.contains(target);
      }
    }
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    let max = this.value;
    let node = this;
    while (node.right) {
      node = node.right;
      max = node.value;
    }
    return max;
  }

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {
    cb(this.value);
    if (this.left) {
      this.left.depthFirstForEach(cb);
    }
    if (this.right) {
      this.right.depthFirstForEach(cb);
    }
  }

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb, queue) {
    queue = queue || [this];
    var tree;
    tree = queue.shift();
    if (!tree) {
      return undefined;
    }
    cb(tree.value);
    if (tree.left) {
      queue.push(tree.left);
    }
    if (tree.right) {
      queue.push(tree.right);
    }
    return tree.breadthFirstForEach(cb, queue);
  }
}

module.exports = BinarySearchTree;
