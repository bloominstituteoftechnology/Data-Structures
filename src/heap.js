class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {
    if(this.storage.length === 0){
      this.storage.push(value);
    }
    else{
      let found = false;
      for(let i = 0; i < this.storage.length && !found; i++){
        if(value > this.storage[i]){
          this.storage.splice(i,0,value);
          found = true;
        }
      }
      if(found === false){
        this.storage.push(value);
      }
    }
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    let val = this.storage.shift();
    return val;
  }

  /* Return the maximal value in the heap
  without removing it */
  getMax() {
    if(this.storage.length > 0){
      return this.storage[0]
    }
  }

  /* Return the size of the heap */
  getSize() {
    return this.storage.length;
  }

  /* Moves the element at the specified index "up"
  the heap by swapping it with its parent if its
  parent value is less than the value located at
  the input index */
  bubbleUp(index) {

  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    
  }
}

module.exports = Heap;
