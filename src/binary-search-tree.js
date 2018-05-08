class BinarySearchTree {
  /* Do not modify the constructor */
  constructor (value) {
    this.value = value
    this.left = null
    this.right = null
  }

  /* Inserts the given value
  Make sure the rules of a binary search
  tree are being adhered to */
  createRoot () {
    this.root = null
  }
  insert (value) {
    var root = this.root

    if (!root) {
      this.root = new BinarySearchTree(value)
      this.value = this.root.value
      return
    }

    let currentNode = root
    let newNode = new BinarySearchTree(value)

    while (currentNode) {
      if (value < currentNode.value) {
        if (!currentNode.left) {
          currentNode.left = newNode
          break
        } else {
          currentNode = currentNode.left
        }
      } else {
        if (!currentNode.right) {
          currentNode.right = newNode
          break
        } else {
          currentNode = currentNode.right
        }
      }
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains (target) {}

  /* Returns the maximum value in the tree
  Should not remove the max value from the tree */
  getMax () {}

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach (cb) {}

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach (cb) {}
}

module.exports = BinarySearchTree
