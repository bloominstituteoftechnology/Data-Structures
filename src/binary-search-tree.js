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
let bro = new BinarySearchTree(value);
 let cur = this;
 while(cur) {
   if(value < cur.value) {
     if(!cur.left) {
       cur.left = bro;
       return;
     } else{
       cur = cur.left;
      }
   } else {
     if(!cur.right) {
       cur.right = bro;
       return;
     } else {
        cur = cur.right;
        }
      }
    }
  }

  /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
  contains(target) {
    let cur = this;
    while(cur) {
      if(target === cur.value) {
        return true;
      }
      if(target > cur.value) {
        cur = cur.right;
      }
      else {
        cur = cur.left
      }
    }
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {
      let cur = this;
      let curMax = cur.value;
       while(cur) {
         if(cur.value > curMax ) {
           curMax = cur.value;
         } else {
           cur = cur.right;
         }
       }
       return curMax;
  }
  breadthFirstForEach() {

  }
  depthFirstForEach() {
    
  }
}

module.exports = BinarySearchTree;