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
    let lastNum = this.storage.length - 1;
    this.bubbleUp(lastNum);
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    if (!this.storage.length) return null;
    if (this.storage.length === 1) {
      return this.storage.shift();
    }
    const max = this.storage.shift();

    this.storage.shift();
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
    let parentIndex = Math.floor((index - 1) / 2);
    let swapper = null;

    while (this.storage[index])
      if (this.storage[parentIndex] < this.storage[index]) {
        swapper = this.storage[parentIndex];
        this.storage[parentIndex] = this.storage[index];
        this.storage[index] = swapper;
      } else {
        break;
      }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    let left = Math.floor(2 * index + 1);
    let right = Math.floor(2 * index + 2);
    let swapper = null;


    // while (right < this.storage.length - 1) {
    if (this.storage[left] > this.storage[index]) {
      swapper = this.storage[index];
      this.storage[index] = this.storage[left];
      this.storage[left] = swapper;
      // index = left;
      // left = Math.floor((index - 1) / 2);
      // right = Math.floor(2 * index + 2);
    }
    if (this.storage[right] > this.storage[index]) {
      swapper = this.storage[index];
      this.storage[index] = this.storage[right];
      this.storage[right] = swapper;
      index = right;
      left = Math.floor((index - 1) / 2);
      right = Math.floor(2 * index + 2);
    } else {
      // index = 0;
      // break;
    }
  }
}

module.exports = Heap;
