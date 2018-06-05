class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

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
    const newNode = new Node(value);
    let current = this;

    while (true) {
      // new value is less than node's value - move left
      if (value < current.value) {
        // no left - new node goes left
        if (current.left === null) {
          current.left = newNode;
          break;
        } else {
          current = current.left;
        }
      }
      // new value is greater than node's value - move right
      else if (value > current.value) {
        // no right - move right
        if (current.right === null) {
          current.right = newNode;
          break;
        } else {
          current = current.right;
        }
      }
      // ignore new value if it is equal to the current one
      else {
        break;
      }
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {}

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {}
}

module.exports = BinarySearchTree;
