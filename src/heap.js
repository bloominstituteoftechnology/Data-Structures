class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {
    const index = this.storage.push(value);
    // this.bubbleUp(index);
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
    // (I-1) /2 IS THE formula to get the parent index
    // grab this nodes(more apropiately called value) parent
    const parentIndex = Math.floor((index - 1/2));
    // checking to see if value 10 is less than value 3 
    if (this.storage[parentIndex] < this.storage[index]) {
      // this line swaps the value at index and parentIndex
      [this.storage[parentIndex], this.storage[index]] = [this.storage[index], this.storage[parentIndex]];
      this.bubbleUp(parentIndex);
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    // siftDown is the opposite of what sean was telling us 
    // when softing down there is 
    const leftChildIndex = index * 2;
    const rightChildIndex = (index * 2)+ 1;
  }
}

module.exports = Heap;
