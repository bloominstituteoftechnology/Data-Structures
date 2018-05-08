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
      //send the value left
      if (!this.left) {
        this.left = newNode;
      } else {
        //recursively call insert
        this.left.insert(value);
      }
    } else if (value >= this.value) {
      if (!this.right) {
        this.right = newNode;
      } else {
        this.right.insert(value);
      }
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    if (this.value === target) return true;
    if (target < this.value) {
      if (this.left) {
        if (this.left.contains(target)) return true;
      }
    }
    else {
      if (this.right) {
        if (this.right.contains(target)) return true;
      }
    } 
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {}

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {
    cb(this.value);
    if(this.left) {
      this.left.depthFirstForEach(cb);
    }
    if(this.right) {
      this.right.depthFirstForEach(cb);
    }
  }

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {
    //import queue or build self
    const q = [];
    // push the current node onto our queue
    q.push(this);
    //iterate through the q until it's empty
    while(q.length > 0) {
      //dequeue the next node in line
      const node = q.shift();
      //add nodes children to queue
      if(node.left) q.push(node.left);
      if(node.left) q.push(node.right);
      cb(node.value);
    }
  }
}

module.exports = BinarySearchTree;
