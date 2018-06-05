class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {

  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {

  }

  /* Return the maximal value in the heap
  without removing it */
  getMax() {

  }

  /* Return the size of the heap */
  getSize() {

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
    let leftChildIndex = index*2+1;
    let rightChildIndex = index*2+2;
    let maxChildIndex;

    if(this.storage[leftChildIndex] && this.storage[rightChildIndex]) {
      maxChildIndex = this.storage[leftChildIndex] > this.storage[rightChildIndex] ? leftChildIndex: rightChildIndex;
    }else if (this.storage[leftChildIndex]) {
      maxChildIndex = leftChildIndex;
    } else if (this.storage [rightChildIndex]) {
      maxChildIndex = rightChildIndex;
    }

    if(this.storage[index] < this.storage[maxChildIndex]) {
      [this.storage[maxChildIndex], this.storage[index]] = [this.storage[index], this.storage[maxChildIndex]];
      this.siftDown(maxChildIndex);
    }
  }
}

module.exports = Heap;
