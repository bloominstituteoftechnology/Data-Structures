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
    this.bubbleUp(index);
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    if (!this.storage.length) return null;
    if (this.storage.length === 1) {
      return this.storage.pop();
    }
    const max = this.storage[0].shift();
    // remove the element with the highest index
    // assign it to this.storage
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
    const parentNode = () => Math.floor((index - 1) / 2);
    let parent = parentNode();
    while(index > 0 && this.storage[index] > this.storage[parent]) {
      [this.storage[index], this.storage[parent]] = [this.storage[parent], this.storage[index]];
      index = parent, parent = parentNode();
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    const leftChild = () => 2 * index + 1;
    const rightChild = () => 2 * index + 2;
    let left = leftChild();
    let right = rightChild();
    while (this.storage[left] || this.storage[right]) {
      let child = this.storage[left] > this.storage[right] ? left : right;
      if (this.storage[index] < this.storage[child]) [this.storage[index], this.storage[child]] = [this.storage[child], this.storage[index]];
      else return;
      index = child, left = leftChild(), right = rightChild();
    }
  }
}

module.exports = Heap;
