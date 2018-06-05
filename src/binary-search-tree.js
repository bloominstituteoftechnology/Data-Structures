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

    if(value > this.value) {
      if(!this.right) {
        this.right = node;
      }
      this.right.insert(value);
    }

    if(value < this.value) {
      if(!this.left) {
        this.left = node;
      }

      this.left.insert(value);
    }

  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    let node = this;

    while(node) {
      if(target === node.value) {
        return true;
      }
      if(target > node.value) {
        node = node.right;
      }
      else {
        node = node.left
      }
    }
    return false;

  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {

  }
}

module.exports = BinarySearchTree;