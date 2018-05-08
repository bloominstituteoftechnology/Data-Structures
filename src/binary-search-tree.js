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
    let currentNode = this;
    while (currentNode) {
      if (value < currentNode.value) {
        if (!currentNode.left) {
          currentNode.left = { value };
          return;
        } else {
          currentNode = this.left;
        }
      } else {
        if (!currentNode.right) {
          currentNode.right = { value };
          return;
        } else {
          currentNode = this.right;
        }
      }
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    let currentNode = this;
    while (currentNode) {
      if (target === currentNode.value) return true;
      if (target < currentNode.value) {
        currentNode = currentNode.left;
      } else {
        currentNode = currentNode.right;
      }
    }
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    let currentNode = this;
    let currentMax = currentNode.value;
    while (currentNode) {
      if (currentNode.value > currentMax) {
        currentMax = currentNode.value;
      } else {
        currentNode = currentNode.right;
      }
    }
    return currentMax;
  }

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {}

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {}
}

module.exports = BinarySearchTree;
