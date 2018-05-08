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

    if (value < this.value) {
      !this.left
      ? this.left = newNode
      : this.left.insert(value);
      } else if (value > this.value) {
        !this.right
        ? this.right = newNode
        : this.right.insert(value);
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    let currentNode = this;
    
    while (currentNode) {
      if (currentNode.value === target) return true;
      
      target < currentNode.value
      ? currentNode = currentNode.left
      : currentNode = currentNode.right;
    }

    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    let max = this.value;
    let currentNode = this;

    while (currentNode) {
      max < currentNode.value
      ? max = currentNode.value
      : currentNode = currentNode.right;
    }

    return max;
  }

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {
    let rootNode = this;

    function traverse(node) {
      if (node) {
        cb(node.value);
        traverse(node.left);
        traverse(node.right);
      }
    }

    traverse(rootNode);
  }

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {
    let queue = [];
    let current = this;

    if (!current) return null;
    queue.push(current);

    while (current = queue.shift()) {
      cb(current.value);

      current.left && queue.push(current.left);
      current.right && queue.push(current.right);
    }

  }
}

module.exports = BinarySearchTree;
