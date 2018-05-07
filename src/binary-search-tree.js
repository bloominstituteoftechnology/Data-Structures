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
      right: null,
      left: null,
    };
    // console.log(this.value, 'this.value');

    const check = node => {
      if (value >= node.value) {
        node.right ? check(node.right) : (node.right = newNode);
      } else if (value < node.value) {
        node.left ? check(node.left) : (node.left = newNode);
      }
    };
    if (!this.value) {
      this.value = value;
    } else {
      check(this);
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    const check = node => {
      if (node.value === target) return true;
      if (target > node.value && node.right) return check(node.right);
      if (target < node.value && node.left) return check(node.left);
      return false;
    };
    return check(this);
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    let max = this.value;
    let node = this;
    while (node.right) {
      node = node.right;
      max = node.value;
    }
    return max;
  }

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {}

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {}
}

module.exports = BinarySearchTree;
