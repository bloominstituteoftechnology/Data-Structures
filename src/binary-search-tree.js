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
    const node = new BinarySearchTree(value);

    if (value < this.value) {
      if (this.left === null ) this.left = node;
      else this.left.insert(value);
    } else {
      if (this.right === null) this.right = node;
      else this.right.insert(value);
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
        if (target === this.value) return true;

    if (target < this.value && this.left !== null) {
      return this.left.contains(target);
    } else if (target > this.value && this.right !== null) {
      return this.right.contains(target);
    } else return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    return this.right === null ? this.value : this.right.getMax();
  }
}

module.exports = BinarySearchTree;