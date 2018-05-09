class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [null];
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
    const max = this.storage[1];
    let curr = 1;
    while (2 * curr + 1 <= this.getSize()) {
      if (this.storage[2 * curr] > this.storage[2 * curr + 1]) {
        this.storage[curr] = this.storage[2 * curr];
        curr = 2 * curr;
      } else {
        this.storage[curr] = this.storage[2 * curr + 1];
        curr = 2 * curr + 1;
      }
    }
    if (2 * curr <= this.getSize())
      this.storage[curr] = this.storage[2 * curr];
    else
      this.storage[curr] = this.storage[this.getSize()];

    this.storage.pop();
    this.bubbleUp(curr);
    
    return max;
  }

  /* Return the maximal value in the heap
  without removing it */
  getMax() {
    return this.storage[1];
  }

  /* Return the size of the heap */
  getSize() {
    return this.storage.length - 1;
  }

  /* Moves the element at the specified index "up"
  the heap by swapping it with its parent if its
  parent value is less than the value located at
  the input index */
  bubbleUp(index) {
    if (index === 1)
      return;
    const parentIndex = Math.floor(index/2);
    if (this.storage[index] > this.storage[parentIndex]) {
      [this.storage[parentIndex], this.storage[index]] = [this.storage[index], this.storage[parentIndex]];
      this.bubbleUp(parentIndex);
    }

  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    let largerChild;
    if (this.storage[2 * index] > this.storage[2 * index + 1])
      largerChild = 2 * index;
    else
      largerChild = 2 * index + 1;
    
      if (this.storage[largerChild] > this.storage[index]) {
        const temp = this.storage[largerChild];
        this.storage[largerChild] = this.storage[index];
        this.storage[index] = temp;
      }
  }
}

module.exports = Heap;
