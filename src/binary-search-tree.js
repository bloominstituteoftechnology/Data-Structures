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
    let thisNode = this;
    // if the data is less than the node insert it to the left of the tree
    if (value < thisNode.value) {
      //if left is null insert node here
      if (thisNode.left === null) thisNode.left = new BinarySearchTree(value);
      //if left is not null, recurr untill null is found
      else this.left.insert(value);
    } else {
      //if right is null insert node here
      if (thisNode.right === null) thisNode.right = new BinarySearchTree(value);
      //if right is not null, recurr untill null is found
      else this.right.insert(value);
    }
    // while (thisNode) {
    //   if (value < thisNode.value) {
    //     if (thisNode.left === null) {
    //       thisNode.left = new BinarySearchTree(value);
    //     }
    //     else thisNode = this.left;
    //   }
    //   else {
    //     if (thisNode.right === null) {
    //       thisNode.right = new BinarySearchTree(value);
    //     }
    //     else thisNode = this.right;
    //   }
    // }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    //if tree is empty return false
    if (this === null) return false;
    //if target is less than the node's value, move left. If greater do the opposite.
    if (target < this.value && this.left) return this.left.contains(target);
    if (target > this.value && this.right) return this.right.contains(target);
    //if target === this.value return true
    if (target === this.value) return true;
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    if (this.right === null) {
      return this.value;
    }
    return this.right.getMax()
    // let max = this.value;
    // if (max < this.value) {
    //   max = this.value;
    //   this.right.getMax();
    // } else if (max > this.value) {
    //   this.getMax();
    // }
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
