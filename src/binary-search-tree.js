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
    // left side
    // if (value < this.value) {
    //   // console.log('value', value, 'this.value', this.value);
    //   if (this.left === null) {
    //     this.left = new BinarySearchTree(value);
    //   }
    // }
    // if (value >= this.left.value) {
    //   console.log('value', value, 'this.left.value', this.left.value);
    //   this.left.right = new BinarySearchTree(value);
    // }
    // // right side
    // if (value >= this.value) {
    //   if (this.right === null) {
    //     this.right = new BinarySearchTree(value);
    //   }
    // }
    // if (value >= this.left.value) {
    //   console.log('value', value, 'this.left.value', this.left.value);
    //   this.left.right = new BinarySearchTree(value);
    // }
    // console.log('tree', this);
    const newNode = new BinarySearchTree(value);
    const addNode = node => {
      if (node.value >= value) {
        if (!node.left) return (node.left = newNode);
        return addNode(node.left);
      }
      if (node.value < value) {
        if (!node.right) return (node.right = newNode);
        return addNode(node.right);
      }
    };
    return addNode(this);
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    let node = this;
    while (node) {
      if (target > node.value) {
        node = node.right;
      } else if (target < node.value) {
        node = node.left;
      } else {
        return true;
      }
    }
    return false;
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
  depthFirstForEach(cb) {
    // const nodeValues = []; // holder arr
    const forEachNode = node => {
      cb(node.value); // execute cb fn with that node's value
      if (node.left) forEachNode(node.left); // if left node exists, call 'forEach' fn on that node
      if (node.right) forEachNode(node.right); // same as above
    };
    forEachNode(this); // inits call 'forEach' fn on the BST
  }

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {
    // const nodeValues = []; // holder arr
    let node = this;
    while (node) {
      cb(node.value);
      if (node.left) cb(node.left.value);
      if (node.right) cb(node.right.value);
      node = this.next;
    }
  }
}

// const newTree = new BinarySearchTree(10);
// newTree.insert(3);
// newTree.insert(30);
// newTree.insert(6);
// newTree.insert(11);
// newTree.insert(1);
// newTree.insert(45);
// console.log('+++++++++', newTree);
// console.log(newTree.contains(3));

module.exports = BinarySearchTree;
