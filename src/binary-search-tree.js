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
  contains(target) {
    let isFound = false;
    let current = this;

    // traverse unless target is found or there is no node to search
    while (!isFound && current) {
      // target is less than current value - go left
      if (target < current.value) {
        current = current.left;
      }
      // target is greater than current value - go right
      else if (target > current.value) {
        current = current.right;
      }
      // target is equal to the current value - target found
      else {
        isFound = true; // change search status
      }
    }
    return isFound; // return the search status
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    let current = this;
    let max;
    // traverse the tree and start at the root
    while (current) {
      // ignore left half of the tree
      // set max equal to the root if no other right-side values exist
      if (current.right === null) {
        max = current.value;
      }
      // jump to the next right-side node
        // current will be null if no other right-side values exist
      current = current.right;
    }
    return max;
  }
}

module.exports = BinarySearchTree;
