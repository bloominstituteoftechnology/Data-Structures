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
    const node = this;
    const newNode = new BinarySearchTree(value);
    if ( value < node.value ) {
      if ( !node.left ) {
        node.left = newNode;
      } else {
        node.left.insert(value);
      }
    }
    if ( value > node.value ) {
      if ( !node.right ) {
        node.right = newNode;
      } else {
        node.right.insert(value);
      }
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    const node = this;
    if (node.value === target)
      return true;
    if (node.left && node.left.contains(target)) 
      return true;
    if (node.right && node.right.contains(target)) 
      return true;
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    const node = this;
    if (node.right === null) 
      return node.value;
    else if (node.right) 
      return node.right.getMax();
  }
}

module.exports = BinarySearchTree;