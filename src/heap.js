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
    let length = this.storage.length - 1;
    this.bubbleUp(length);
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {}

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
    //grab parents value
    const parentIndex = Math.floor((index - 1) / 2);
    //check to see if the value at this index needs to be shifted up
    if (this.storage[parentIndex] < this.storage[index]) {
      [this.storage[parentIndex], this.storage[index]] = [
        this.storage[index],
        this.storage[parentIndex]
      ];
      //recursively call bubbleup again incase we need to continue shifting up the value up the heap
      this.bubbleUp(parentIndex);
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    const leftChildIndex = index * 2 + 1;
    const rightChild = index * 2 * 2;
  }
}

module.exports = Heap;
