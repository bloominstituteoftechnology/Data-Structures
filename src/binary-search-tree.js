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
    let temp = this;
    const newLeaf = { value: value, left: null, right: null };

    while (temp) {
      if (value < temp.value) {
        if (temp.left === null) {
          temp.left = newLeaf;
          return;
        } 
        temp = temp.left;
      } else if (value > temp.value) {
        if (temp.right === null) {
          temp.right = newLeaf;
          return;
        }
        temp = temp.right;
      } else {
        return; 
      }
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    let temp = this;
  

    while (temp) {
      if (target < temp.value) {
        if (temp.left === null) {    
          return false;
        } 
        temp = temp.left;
      } else if (target > temp.value) {
        if (temp.right === null) {
          return false;
        }
        temp = temp.right;
      } else {
        return true; 
      }
    }
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    let temp = this;

    while (temp) {
       if(temp.right) {
         temp = temp.right;
      } else {
        return temp.value;
      }
    }
  }
}

module.exports = BinarySearchTree;