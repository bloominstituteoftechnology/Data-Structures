class BinarySearchTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    if(value >= this.value) {
      if(!this.right){
        this.right = new BinarySearchTree(value);
      }else{
        this.right.insert(value);
      }
    }else if(value < this.value) {
      if(!this.left){
        this.left = new BinarySearchTree(value);
      }else{
        this.left.insert(value);
      }
    }
  }

  contains(target) {
    if(this.value === target) {
      return true;
    }else if(target > this.value){
      if(!this.right){
        return false;
      }else {
        return this.right.contains(target);
      }
    }else if(target< this.value){
      if(!this.left){
        return false;
      }else{
        return this.left.contains(target)
      }
    }
  }

  getMax() {
    if(this.right){
      return this.right.getMax()
    }else{
      return this.value;
    }
  }
}

const myBST = new BinarySearchTree(5);
//TEST insert
// myBST.insert(2);
// myBST.insert(3);
// myBST.insert(7);
// myBST.insert(6);
// console.log('3:', myBST.left.right.value);
// console.log('6:', myBST.right.left.value);

//TEST contains
// myBST.insert(2);
// myBST.insert(3);
// myBST.insert(7);
// console.log('True:', myBST.contains(7));
// console.log('False:', myBST.contains(8));

//TEST getMax
// console.log('5:', myBST.getMax());
// myBST.insert(30);
// console.log('30:', myBST.getMax());
// myBST.insert(300);
// myBST.insert(3);
// console.log('300:', myBST.getMax());
