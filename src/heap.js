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
    console.log(this.storage);
    let maxVal = this.storage[0];
    this.storage.shift();
    this.siftDown(0);
    return maxVal;
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
    let parentInd = Math.floor((index - 1) / 2);
    let swapper = null;

    while (index > 0) {
      if (this.storage[index] > this.storage[parentInd]) {
        swapper = this.storage[index];
        this.storage[index] = this.storage[parentInd];
        this.storage[parentInd] = swapper;
        index = parentInd;
        parentInd = Math.floor((index - 1) / 2);
      } else {
        break;
      }
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

    while (index < this.storage.length - 1) {
      if (this.storage[left] > this.storage[index]) {
        console.log("swapping left!");
        swapper = this.storage[index];
        this.storage[index] = this.storage[left];
        this.storage[left] = swapper;
        index = left;
        left = Math.floor((index - 1) / 2);
        right = Math.floor(2 * index + 2);
      } else if (this.storage[right] > this.storage[index]) {
        console.log("swapping right!");
        swapper = this.storage[index];
        this.storage[index] = this.storage[right];
        this.storage[right] = swapper;
        index = right;
        left = Math.floor((index - 1) / 2);
        right = Math.floor(2 * index + 2);
      } else {
        break;
      }
    }
  }
}

module.exports = Heap;
