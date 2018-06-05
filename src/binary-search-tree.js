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
    while (currentNode) {
      if (value < currentNode.value && currentNode.left !== null) {
        currentNode = currentNode.left;
      } else if (value < currentNode.value) {
        currentNode.left = newNode;
        break;
      } else if (value > currentNode.value && currentNode.right !== null) {
        currentNode = currentNode.right;
      } else if (value > currentNode.value) {
        currentNode.right = newNode;
        break;
      } else break;
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    let currentNode = this;
    while (currentNode) {
      if (target < currentNode.value && currentNode.left !== null) {
        currentNode = currentNode.left;
      } else if (target > currentNode.value && currentNode.right !== null) {
        currentNode = currentNode.right;
      }

      if (currentNode.value === target) return true;

      if (!currentNode.right && !currentNode.left) return false;
    }
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    if (!this) return null;
    // Recursive
    // if(!this.right){
    //   return this.value
    // }
    // return this.right.getMax();

    // Iterative (I wrote it)
    let currentNode = this;
    while (currentNode.right) {
      currentNode = currentNode.right;
    }
    return currentNode.value;
  }
}

module.exports = BinarySearchTree;
