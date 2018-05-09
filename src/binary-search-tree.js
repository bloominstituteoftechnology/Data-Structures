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
    // {
    //   value: value,
    //   right: null,
    //   left: null,
    // };
    // console.log(this.value, 'this.value');
    const newNode = new BinarySearchTree(value);
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
    let node = this;
    while (node.right) {
      node = node.right;
    }
    return node.value;
  }

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {
    cb(this.value);
    if (this.left) {
      this.left.depthFirstForEach(cb);
    }
    if (this.right) {
      this.right.depthFirstForEach(cb);
    }
  }

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {
    const q = [];
    q.push(this);
    while (q.length > 0) {
      const node = q.shift();
      if (node.left) q.push(node.left);
      if (node.right) q.push(node.right);
      cb(node.value);
    }
  }
}

module.exports = BinarySearchTree;
