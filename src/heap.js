class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {}

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {}

  /* Return the maximal value in the heap
  without removing it */
  getMax() {}

  /* Return the size of the heap */
  getSize() {}

  /* Moves the element at the specified index "up"
  the heap by swapping it with its parent if its
  parent value is less than the value located at
  the input index */
  bubbleUp(index) {
    // grab this element's parent
    const parentIndex = Math.floor((index - 1) / 2);
    // check if index should be shifted up according to parentIndex value
    if (this.storage[parentIndex] < this.storage[index]) {
      // swap index and parent index
      [this.storage[parentIndex], this.storage[index]] = [
        this.storage[index],
        this.storage[parentIndex],
      ];
      // recursively call bubbleUp again to continue shifting index up the heap if needed
      this.bubbleUp(parentIndex);
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    const leftChildIndex = index * 2 + 1;
    const rightChildIndex = Index * 2 + 2;
    // opposite of bubbleUp
  }
}

module.exports = Heap;
