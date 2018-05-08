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
    if (value > this.value) {
      //insert right or below right
      if (!this.right) this.right = newNode;
      else this.right.insert(value);
    } else if (value < this.value) {
      //insert left or below left
      if (!this.left) this.left = newNode;
      else this.left.insert(value);
    } else {
      //value == this.value, dont add
      return null;
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    //check main node
    console.log(this.value);
    if (target === this.value) return true;
    else if (target > this.value) {
      if (this.right) this.right.contains(target);
      else return false;
    } else {
      if (this.left) this.left.contains(target);
      else return false;
    }
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {}

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
