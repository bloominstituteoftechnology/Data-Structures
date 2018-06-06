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
    const newNode = new BinarySearchTree(value);
    let node = this;

    while (node) {
      if (value < node.value) {
        if (!node.left) {
          node.left = newNode;
          return;
        }
        node = node.left;
      }
      if (!node.right) {
        node.right = newNode;
        return;
      }
      node = node.right;
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
