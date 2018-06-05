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
    this.bubbleUp(this.getSize() - 1);
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    const max = this.storage.shift();
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
    const parent = () => Math.floor((index - 1) / 2);
    let p = parent();
    while(i > 0 && this.storage[i] > this.storage[p]) {
      [this.storage[i], this.storage[p]] = [this.storage[p], this.storage[i]];
      i = p, p = parent();
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
      index = child, left = leftChild(), right = rightChild();
    }
  }
}

module.exports = Heap;
