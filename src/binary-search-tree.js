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
    let leaf = this
    let newLeaf = { value, left: null, right: null }

    while (leaf) {
      if (value < leaf.value) {
        if (!leaf.left) {
          leaf.left = newLeaf
          return
        }
        leaf = leaf.left
      } else if (value > leaf.value) {
        if (!leaf.right) {
          leaf.right = newLeaf
          return
        }
        leaf = leaf.right
      } else return
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(value) {
    let leaf = this

    while (leaf) {
      if (value < leaf.value) {
        if (!leaf.left) {
          return false
        }
        leaf = leaf.left
      } else if (value > leaf.value) {
        if (!leaf.right) {
          return false
        }
        leaf = leaf.right
      } else return true
    }
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    let leaf = this

    while (leaf) {
      if (leaf.right) {
        leaf = leaf.right
      } else return leaf.value
    }
  }
}

module.exports = BinarySearchTree;