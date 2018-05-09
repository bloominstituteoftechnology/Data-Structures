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
    let self = this;
    while (self) {
      if (self.value > value) {
        if (!self.left) {
          self.left = { value };
          return;
        } else {
          self = self.left;
        }
      } else {
        if (!self.right) {
          self.right = { value };
          return;
        } else {
          self = self.right;
        }
      }
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    let self = this;
    while (self) {
      if (target === self.value) return true;
      if (target < self.value) {
        self = self.left;
      } else {
        self = self.right;
      }
    }
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    let self = this;
    let currentMax = self.value;
    while (self) {
      if (self.value > currentMax) {
        currentMax = self.value;
      } else {
        self = self.right;
      }
    }
    return currentMax;
  }

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {
    let self = this;
    const traverse = node => {
      cb(node.value);
      node.left && traverse(node.left);
      node.right && traverse(node.right);
    };
    traverse(self);
  }

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {
    let self = this;
    let queue = [self];
    while ((self = queue.shift())) {
      cb(self.value);
      self.left && queue.push(self.left);
      self.right && queue.push(self.right);
    }
  }
}

module.exports = BinarySearchTree;
