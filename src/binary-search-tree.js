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
    if (value < this.value) {
      // add the new node as the left child if one doesn't exist
      if (!this.left) {
        this.left = newNode;
      } else {
        //call insert over and over from itself.
        this.left.insert(value);
      }
    } else if (value >= this.value) {
      if (!this.right) {
        this.right = newNode;
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
    if (this.value === target) {
      return true;
    } 
    if (target < this.value) {
      if (this.left) {
        if (this.left.contains(target)) {
          return true;
        } 
      }
    } else {
      if (this.right) {
        if (this.right.contains(target)) {
          return true;
        } 
      }
    }
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    if (!this) {
      return null;
    } 
    let max = this.value;
    let current = this;

    while (current) {
      if (current.value > max) {
        max = current.value;
      }
      current = current.right;
    }

    return max;
  }
}

module.exports = BinarySearchTree;