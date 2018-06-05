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
      if (!this.right) {
        this.right = new BinarySearchTree(value);
      } else {
        this.right.insert(value);
      }
    } else {
      if (!this.left) {
        this.left = new BinarySearchTree(value);
      } else {
        this.left.insert(value);
      }
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    if (this.value === target) return true;
    if (this.value > target) {
      if (this.left) {
        return this.left.contains(target);
      }
    } else {
      if (this.right) {
        return this.right.contains(target);
      }
    }
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    if (!this.right && !this.left) return this.value;
    else if (this.right) return this.right.getMax();
    else if (this.left.value > this.value) return this.left.getMax();
  }
}

module.exports = BinarySearchTree;
