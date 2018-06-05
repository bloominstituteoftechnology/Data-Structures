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
    const deleted = this.storage.shift();
    this.siftDown(0);
    return deleted;
  }

  /* Return the maximal value in the heap
  without removing it */
  getMax() { return Math.max(...this.storage) }

  /* Return the size of the heap */
  getSize() { return this.storage.length }

  /* Moves the element at the specified index "up"
  the heap by swapping it with its parent if its
  parent value is less than the value located at
  the input index */
  bubbleUp(index) {
    const arr = this.storage;
    const parentIdx = Math.floor((index - 1) / 2);

    if (arr[index] > arr[parentIdx]) {
      [arr[index], arr[parentIdx]] = [arr[parentIdx], arr[index]];
      this.bubbleUp(parentIdx);
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    const arr = this.storage;
    const leftIdx = index * 2 + 1;
    const rightIdx = index * 2 + 2;

    if (arr[rightIdx] && arr[rightIdx] > arr[index]) {
      [arr[rightIdx], arr[index]] = [arr[index], arr[rightIdx]];
      this.siftDown(rightIdx);
    } else if (arr[leftIdx] && arr[leftIdx] > arr[index]) {
      [arr[leftIdx], arr[index]] = [arr[index], arr[leftIdx]];
      this.siftDown(leftIdx);
    }
  }
}

module.exports = Heap;
