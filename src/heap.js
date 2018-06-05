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
    console.log(this.storage);
    this.bubbleUp(this.getSize() - 1);
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {

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
    let bubbling = true;
    let temp;
    while (bubbling === true) {
      let parentIndex = Math.floor((index - 1) / 2);
      if (this.storage[index] > this.storage[parentIndex]) {
        temp = this.storage[index];
        this.storage[index] = this.storage[parentIndex];
        this.storage[parentIndex] = temp;
        index = parentIndex;
      } else {
        bubbling = false;
      }
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {

  }
}

module.exports = Heap;
