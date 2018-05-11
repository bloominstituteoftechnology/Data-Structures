class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {
    // insert the value at the end of the storage array
    const index = this.storage.push(value) - 1;
    this.bubbleUp(index);
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    // check to see if the heap is not empty
    if (!this.storage.length) return null;
    // check to see if the heap only has one element
    if (this.storage.length === 1) {
      return this.storage.pop();
    }

    const max = this.storage[0];
    // move the last element in the heap to the root temporarily
    this.storage[0] = this.storage.pop();
    // call siftDown on the root element to re-arrange the heap
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
    // grab this value's parent
    const parentIndex = Math.floor((index - 1) / 2);
    // check to see if the value at this index needs to be shifted up
    if (this.storage[parentIndex] < this.storage[index]) {
      // swap the values at index and parentIndex
      [this.storage[parentIndex], this.storage[index]] = [this.storage[index], this.storage[parentIndex]];
      // recursively call bubbleUp again in case we need to continue shifting
      // the value up the heap
      this.bubbleUp(parentIndex);
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    // grab the value's two children 
    const leftChildIndex = index * 2 + 1;
    const rightChildIndex = index * 2 + 2;
    // figure out the larger child
    let maxChild;
    
    if (this.storage[leftChildIndex] && this.storage[rightChildIndex]) {
      maxChild = this.storage[leftChildIndex] > this.storage[rightChildIndex] ? leftChildIndex : rightChildIndex;
    } else if (this.storage[leftChildIndex]) {
      maxChild = leftChildIndex;
    } else if (this.storage[rightChildIndex]) {
      maxChild = rightChildIndex;
    } 

    // check to see if we need to swap our current value with its larger child
    if (this.storage[index] < this.storage[maxChild]) {
      [this.storage[maxChild], this.storage[index]] = [this.storage[index], this.storage[maxChild]];
      // recursively call siftDown in case we need to keep moving the element down the heap
      this.siftDown(maxChild);
    }
  }
}

module.exports = Heap;
