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
      if (node.value < current.value) {
        if (!current.left) {
          current.left = node;
          break;
        } current = current.left;
      } else if (node.value > current.value) {
        if (!current.right) {
          current.right = node;
          break;
        } current = current.right;
      } else {
        break;
      }
    }
  };

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    const checkCurrent = (current) => {
      if (target === current.value) {
        return true;
      } if (target > current.value) {
        if (!current.right) return false;
        else return checkCurrent(current.right);
      } if (target < current.value) {
        if (!current.left) return false;
        else return checkCurrent(current.left);
      }
    }; return checkCurrent(this);
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax(current=this) {
    if (!current.right) return current.value;
    return this.getMax(current.right);
  }
  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {
    let queue = [];
    const traverseAndCb = (current) => {
      cb(current.value);
      if (current.right) {
        queue.push(current.right);
      } if (current.left) {
        return traverseAndCb(current.left)
      } if (!queue.length) return;
      else {
        traverseAndCb(queue.pop());
      }
    }; traverseAndCb(this);
  }

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {
    let queue = [];
    //push left and right of root to queue
    const traverseAndCb = (current) => {
      cb(current.value);
      if (current.left) {
        queue.push(current.left);
      } if (current.right) {
        queue.push(current.right);
      } if (!queue.length) return;
      else {
        return traverseAndCb(queue.shift());
      }
    }; traverseAndCb(this);
    //traverse via shift
    //push left and right of each in queue
  }
}

module.exports = BinarySearchTree;