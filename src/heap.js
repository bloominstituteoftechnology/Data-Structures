class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {
    this.storage.push(value);
   
    this.bubbleUp(this.storage.length - 1);
    // while (last > 0) {

    // }
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    let result = this.storage.shift();
    this.siftDown(0)
    return result

  }

  /* Return the maximal value in the heap
  without removing it */
  getMax() {
    let maxNode = this.storage[0];
    return maxNode
  }

  /* Return the size of the heap */
  getSize() {
    let last = this.storage.length;
    return last
  }

  /* Moves the element at the specified index "up"
  the heap by swapping it with its parent if its
  parent value is less than the value located at
  the input index */
  bubbleUp(index) {
    let nodeValue = this.storage[index];
    // while (index > 0) { 
      let parentIndex = Math.floor((index + 1) / 2) - 1,
      parent = this.storage[parentIndex],
      child = this.storage[index];
      if (child > parent) {
        [this.storage[parentIndex], this.storage[index] ]= [this.storage[index], this.storage[parentIndex]];
        this.bubbleUp(parentIndex);
      }
      
    // }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    const leftChildIndex = index * 2 + 1;
    const rightChildIndex = index * 2 + 2;
    let maxChildIndex;
    //Check to see if the values exist at both of the indices
    if (this.storage[leftChildIndex] && this.storage[rightChildIndex]) {
      maxChildIndex = this.storage[leftChildIndex] > this.storage[rightChildIndex] ? leftChildIndex : rightChildIndex; //missing
    } else if (this.storage[leftChildIndex]) {
      maxChildIndex = leftChildIndex;
    }
     else if (this.storage[rightChildIndex]) {
      maxChildIndex = rightChildIndex;
    }
    //Check to see if we need to swap our current value with the value
    //located at maxChildIndex
    if (this.storage[index] < this.storage[maxChildIndex]) {
      //SWAP them
      [this.storage[maxChildIndex], this.storage[index] ]= [this.storage[index], this.storage[maxChildIndex]] ;//missing
      this.siftDown(maxChildIndex);
    }
  }
}

module.exports = Heap;