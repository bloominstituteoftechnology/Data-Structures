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
    const nbst = new BinarySearchTree(value);
    if (value > this.value) {
      if(!this.right) {
        this.right = nbst;
      } else {
        this.right.insert(value);
      }
      } else {
        if(!this.left) {
          this.left = nbst;
        } else {
          this.left.insert(value);
        }
      }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    let current = this;
    let found = false;
    while(!found && current) {
      if(target > current.value) {
        current = current.right;
      } else if (target < current.value) {
        current = current.left;
      } else {
        found = true;
      }
    }
    return found;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    let max = null;
    if(this.right === null && this.left === null) {
      max = this.value;
      return max;
    } else if(this.right) {
      return this.right.getMax();
    } else {
      if(this.left.value > this.value) {
        return this.left.getMax();
      }
    }
  }

  // was not included NOT REQUIRED
  depthFirstForEach() {
  }

  //was not included NOT REQUIRED
  breadthFirstForEach() {
  }
  
}

module.exports = BinarySearchTree;