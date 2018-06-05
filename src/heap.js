class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {
    if (value > this.getMax()) this.storage.unshift(value);
    else {
      this.storage.push(value);
      let index = this.getSize();
      this.bubbleUp(index);
    }
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    let max = this.getMax();
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
    let parent = Math.floor((index - 1) / 2);
    if (this.storage[index] > this.storage[parent]) {
      [this.storage[parent], this.storage[index]] = [
        this.storage[index],
        this.storage[parent]
      ];
      this.bubbleUp(parent);
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    let left = 2 * index + 1;
    let right = 2 * index + 2;
    let child = this.storage[left] >= this.storage[right] ? left : right;
    if (this.storage[index] < this.storage[child]) {
      [this.storage[index], this.storage[child]] = [
        this.storage[child],
        this.storage[index]
      ];
      this.siftDown(child);
    }
  }
}

module.exports = Heap;
