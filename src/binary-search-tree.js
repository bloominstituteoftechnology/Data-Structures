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
    let node = {
      value: value,
      left: null,
      right: null
    };
    if (value < this.value) {
      this.left = node;
    } else if (value > this.value) {
      this.right = node;
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
