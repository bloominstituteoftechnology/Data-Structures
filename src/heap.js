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
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    const oldMax = this.storage.shift();
    this.siftDown(0);
    return oldMax;
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
    const parentIndex = Math.floor((index - 1) / 2);

    if (this.storage[parentIndex] < this.storage[index]) {
      [this.storage[parentIndex], this.storage[index]] = [this.storage[index], this.storage[parentIndex]]
      this.bubbleUp(parentIndex);
    } 
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    const leftChildIndex = index * 2 + 1;
    const rightChildIndex = index * 2 + 2;
    let maxChildIndex;

    if (this.storage[leftChildIndex] && this.storage[rightChildIndex]) {
      maxChildIndex = this.storage[leftChildIndex] > this.storage[rightChildIndex] ? leftChildIndex : rightChildIndex;
    } else if (this.storage[leftChildIndex]) {
      maxChildIndex = leftChildIndex;
    } else if (this.storage[rightChildIndex]) {
      maxChildIndex = rightChildIndex;
    }

    if (this.storage[index] < this.storage[maxChildIndex]) {
      [this.storage[maxChildIndex], this.storage[index]] = [this.storage[index], this.storage[maxChildIndex]];
      this.siftDown(maxChildIndex);
    }
  }
}

module.exports = Heap;
