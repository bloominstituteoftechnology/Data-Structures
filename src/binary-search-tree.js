class BinarySearchTree {
  /* Do not modify the constructor */
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
  }

  /* Inserts the given value
  Make sure the rules of a binary search
  tree are being adhered to */
  insert(value) {
    let cur = this
    const node = {
      value,
      left: null,
      right: null
    }
    while (cur) {
      if (value < cur.value) {
        if (!cur.left) {
          cur.left = node
          return
        }
        cur = cur.left
      } else if (value > cur.value) {
        if (!cur.right) {
          cur.right = node
          return
        }
        cur = cur.right
      } else return
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    if (this.value === target) return true
    let cur = this
    while (cur) {
      if (target < cur.value) {
        if (!cur.left) {
          return false
        }
        cur = cur.left
      } else if (target > cur.value) {
        if (!cur.right) {
          return false
        }
        cur = cur.right
      } else return true
    }
    return false
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    if (!this) return null

    let max = this.value,
      cur = this
    while (cur) {
      !cur.right ? (max = cur.value) : (cur = cur.right)
    }
    return max
  }
}

module.exports = BinarySearchTree
