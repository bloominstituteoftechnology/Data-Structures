class Node {
  constructor() {
    this.root = null;
  }
}

class BinarySearchTree {
  /* Do not modify the constructor */
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
    this.root = null;
  }

  /* Inserts the given value
  Make sure the rules of a binary search
  tree are being adhered to */
  insert(value) {

    const newNode = new BinarySearchTree(value);
    if (value < this.value) {
      if (!this.left) {
        this.left = newNode;
      } else {
        this.left.insert(value);
      }
    } else if (value >= this.value) {
      if (!this.right) {
        this.right = newNode;
      } else {
        this.right.insert(value)
      }
    }
    // Node.root 
    // let newNode = {value};
    // if (this.value === null) {
    //   this.value = value;
    // } else {
    //   this.right = value
    // };



    // if (Node.root === null) {
    //   Node.root = newNode;
    // }
    //  else {
    // }
    // if (!this.value) {
    //   this.value = newNode;
    // } else {
    //   this.right = newNode;
    // }
    // return this
    // if (this.root === null) {
    //   this.root = newNode;
    // } else {

    // }
    // while (newNode) {

    // }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    if (this.value === target) {
      return true;
    }
    if (this.left) {
      if (this.left.contains(target)) {
        return true;
      }

    }
    if (this.right) {
      if (this.right.contains(target)) {
        return true;
      }
    }
    return false;


    // this.root = this.removeNode(this.root, target)
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    if (!this) return null;
    //recursive
    if (!this.right) {
      return this.value;
    }
    return this.right.getMax();

    //iterative
    // let current = this;
    // while (current.right) {
    //   current = current.next;
    // }
    // return current.value


//     let last = this.root[this.root.length - 1];
// return last;
  }
}

module.exports = BinarySearchTree;