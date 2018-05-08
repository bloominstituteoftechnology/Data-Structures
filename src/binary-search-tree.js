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
    let currentNode = this;
    while (currentNode) {
      if (value < currentNode.value) {
        if (!currentNode.left) {
          currentNode.left = { value, left: null, right: null };
          return;
        } else {
          currentNode = this.left;
        }
      } else {
        if (!currentNode.right) {
          currentNode.right = { value, left: null, right: null };
          return;
        } else {
          currentNode = this.right;
        }
      }
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
      if (target < currentNode.value) {
        currentNode = currentNode.left;
      } else {
        currentNode = currentNode.right;
      }
    }
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    let max = this.value;
    let currentNode = this;
    while (currentNode) {
      if (currentNode.value > max) max = currentNode.value;
      else {
        currentNode = currentNode.right;
      }
    }
    return max;
  }

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {
    let currentNode = this;

    function depthFirst(node) {
      if (!node) return null;
      cb(node.value);
      depthFirst(node.left);
      depthFirst(node.right);
    }
    depthFirst(currentNode);
  }
  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {
    var current = [this];
    while (current.length > 0) {
      let next = [];
      current.forEach(node => {
        cb(node.value);
        if (node.left) next.push(node.left);
        if (node.right) next.push(node.right);
      });
      current = next;
    }
  }
}

module.exports = BinarySearchTree;
