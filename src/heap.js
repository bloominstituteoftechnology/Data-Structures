class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {
    const index = this.storage.push(value) - 1;
    this.bubbleUp(index)
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    //check if heap is empty
    if (!this.storage.length) return null;
    //check if heap has only one element
    if (this.storage.length === 1) {
      return this.storage.pop();
    }
    const max = this.storage[0];
    this.storage[0] = this.storage.pop();
    this.siftDown(0);
    return max;
  }

  /* Return the maximal value in the heap
  without removing it */
  getMax() {
    return this.storage[0];
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
    //grab this nodes parent 
    const parentIndex = Math.floor((index - 1)/2);
    //check to see if value at this index must be bubled up
    if(this.storage[parentIndex] < this.storage[index]) {
      [this.storage[parentIndex], this.storage[index]] = [this.storage[index], this.storage[parentIndex]];
      //recursively call the function
      this.bubbleUp(parentIndex);
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    //grab the values two children
    const leftChildIndex = index * 2 + 1
    const rightChildIndex = index * 2 + 2
    //figure out the larger child
    let maxChild;
    if(this.storage[leftChildIndex]) {
      if(!this.storage[rightChildIndex]) {
        maxChild = leftChildIndex;
      } else if(this.storage[rightChildIndex]) {
        maxChild = this.storage[leftChildIndex] > this.storage[rightChildIndex] ? leftChildIndex : rightChildIndex;
      }
      // check to see if we need to swap current value its larger child
      if(this.storage[index] < this.storage[maxChild]){
        [this.storage[maxChild], this.storage[index]] = [this.storage[index], this.storage[maxChild]];
      }
    }
  }
}

module.exports = Heap;
