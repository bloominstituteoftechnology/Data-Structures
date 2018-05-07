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
    let curr = this;

    while (curr) {
      if (value > curr.value){
        if (curr.right)
          curr = curr.right;
        else {
          curr.right = new BinarySearchTree(value);
          curr = null;
        }
      } else {
        if (curr.left)
          curr = curr.left;
        else {
          curr.left = new BinarySearchTree(value);
          curr = null;
        }
      }
    }

  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    let curr = this;
    while (curr) {
      if (curr.value === target)
        return true;
      if (target > curr.value){
        if (curr.right)
          curr = curr.right;
        else
          return false;
      } else {
        if (curr.left)
          curr = curr.left;
        else
          return false;
      }

    }
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    let curr = this;
    while(curr) {
      if (curr.right)
        curr = curr.right;
      else
        return curr.value;
    }
  }

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {

    function executeCb(curr) {
      cb(curr.value);
      if (!curr.right && !curr.left)
        return;
      if (curr.left)
        executeCb(curr.left)

      if (curr.right)
        executeCb(curr.right);
    }

  executeCb(this);

  }

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {

  }
}

module.exports = BinarySearchTree;