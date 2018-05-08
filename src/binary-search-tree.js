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
    let current = this;
    while (current !== null) {
      console.log(this);
      if (node.value < current.value) {
        if (!current.left) {
          current.left = node;
          break;
        }
        current = current.left;
      } else if (node.value > current.value) {
        if (!current.right) {
          current.right = node;
          break;
        }
        current = current.right;
      } else {
        break;
      }
    }

  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    const current = this.root;
    while (current) {
      if (target === current.target) {
        return true;
      }
      if (target < current.target) {
        current = current.left;
      } else {
        current = current.right;
      }
    }
    return false;

  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {


  }

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {

  }

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {

  }
}

module.exports = BinarySearchTree;