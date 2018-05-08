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
    if(!this.value){
      this.value = value;
    }
    else if(value < this.value){
      if(!this.left){
        this.left = new BinarySearchTree(value);
      }
      else{
        this.left.insert(value);
      }
    }
    else{
      if(!this.right){
        this.right = new BinarySearchTree(value);
      }
      else{
        this.right.insert(value);
      }
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    let current = this;
    while(current.value){
      if(current.value === target){
        return true;
      }
      else if(target < current.value){
        if(!current.left){
          return false;
        }
        else{
          current = this.left;
        }
      }
      else{
        if(!current.right){
          return false;
        }
        else{
          current = this.right;
        }
      }
    }
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
    if(this.value){
      if(this.right){
        return this.right.getMax();
      }
      else{
        return this.value;
      }
    }
    else{
      return null;
    }
  }

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {
    let s = [];
    s.push(this);
    let current = null;
    while(s.length > 0){
      current = s.pop();
      cb(current.value);
      if(current.right){
        s.push(current.right);
      }
      if(current.left){
        s.push(current.left);
      }
    }
  }

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {
    let q = [];
    q.push(this);
    let current = null;
    while(q.length > 0){
      current = q.shift();
      if(current){
        q.push(current.left);
        q.push(current.right);
        cb(current.value);
      }
    }
  }
}

module.exports = BinarySearchTree;
