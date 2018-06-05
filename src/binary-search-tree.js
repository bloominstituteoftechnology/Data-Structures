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
    const newNode = {
      value: value,
      left: null,
      right: null
    };

    let currentNode = this;

    while (true) {
      if (value >= currentNode.value) {
        if (!currentNode.right) {
          currentNode.right = newNode;
          return
        } else {
          currentNode = currentNode.right
        } 

      } else {
        if (!currentNode.left) {
          currentNode.left = newNode;
          return
        } else {
          currentNode = currentNode.left
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

    while (true) {
      if (target > currentNode.value) {
        if (!currentNode.right) {
          return false
        } else {
          currentNode = currentNode.right
        } 

      } else if (target < currentNode.value) {
        if (!currentNode.left) {
          return false
        } else {
          currentNode = currentNode.left
        } 
      } else {
        return true;
      }
    } 
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    let currentNode = this;

    while (currentNode.right) { 
      currentNode = currentNode.right;
    } 
    return currentNode.value; 
  }
}

module.exports = BinarySearchTree;
