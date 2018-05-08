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
    console.log(this.value);
    console.log(value);

    // // CASE #1: If the top node value is not defined, then set it to the value of the input.
    if (!this.value) {
      this.value = value;
      return 'Your first node has been added!';
    }
    // CASE #1: If myB.left is empty and the inputted value is less than this.value, then insert
    // this new node at myB.left.value.
    if (value < this.value) {
      if (!this.left) {
        this.left = newNode;
      } else {
        this.left.insert(value);
      }
      // CASE #2: If myB.right is empty and the inputted value is less than this.value, then insert
      // this new node at myB.right.value.
    } else {
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
    // LOGIC APPROACH: Establish all circumstances that will return 'true', then return 'false' for all other cases

    // CASE #1: Only 1 element in tree, and that element is equal to target
    if (this.value === target) {
      console.log('Case #1');
      return true;
    }
    // CASE #2 if this.left exists AND 'target' is equal to this.value somewhere in that tree, then return true.
    if (this.left && this.left.contains(target)) {
      console.log('Case #2');
      return true;
    }
    // CASE #3 if this.right exists AND 'target' is equal to this.value somewhere in that tree, then return true.
    if (this.right && this.right.contains(target)) {
      console.log('Case #3');
      return true;
    }
    return false;
  }

  /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
  getMax() {}

  /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
  depthFirstForEach(cb) {}

  /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
  breadthFirstForEach(cb) {}
}

module.exports = BinarySearchTree;

// ========= myB instance created ======== //
const myB = new BinarySearchTree();
// ========= data added to myB using insert() ======= //
myB.insert(100);
console.log(myB);
myB.insert(70);
console.log(myB);
myB.insert(60);
myB.insert(50);
myB.insert(51);
myB.insert(61);
myB.insert(71);
myB.insert(120);
myB.insert(140);
myB.insert(139);
myB.insert(119);
// ====== visualization of data structure ======= //
console.log(myB.right);
console.log(myB.right);
console.log(myB.right.value);
// ====== contains() method ======= //
console.log(myB.contains(71));
