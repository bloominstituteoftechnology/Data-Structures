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
    // if value is greater than the current node, go to the right
    // if there is no node to the right, insert the a new BST
    // if the vlaue is less than the current node, go to the left.
    // if there is nothing to the left, insert the node, otherwise keep going
    if (value >= this.value) {
      if (!this.right) this.right = new BinarySearchTree(value);
      else this.right.insert(value);
    }
    else { 
        if (!this.left) this.left = new BinarySearchTree(value);
        else this.left.insert(value);
      }
    }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    // if target === the current node value, return true
    if (this.value === target) return true;
    // Check left side
    if (this.left && this.left.contains(target)) return true;
    // check right side
    if (this.right && this.right.contains(target)) return true;
    // false if nothing else
    return false
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {

  }
}

module.exports = BinarySearchTree;