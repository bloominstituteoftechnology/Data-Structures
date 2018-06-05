class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {

  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {

  }

  /* Return the maximal value in the heap
  without removing it */
  getMax() {

  }

  /* Return the size of the heap */
  getSize() {

  }

  /* Moves the element at the specified index "up"
  the heap by swapping it with its parent if its
  parent value is less than the value located at
  the input index */
  bubbleUp(index) {

  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    //grab the two indices that correspond with this index
    const leftChildIndex = index * 2 + 1;
    const rightChildIndex = index * 2 + 2;
    //figure out the larger child
    let maxChild;

    if(this.storage[leftChildIndex] && this.storage[rightChildIndex]) {
      maxChildIndex = this.storage[leftChildIndex] > this.storage[rightChildIndex] ?
    } else if (this.storage[leftChildIndex]) {
      maxChildIndex = leftChildIndex;
    } else if (this.storage[rightChildIndex]) {
      maxChildIndex = rightChildIndex;
    }

    //check to see if we need to swap our current value with the vallue
    //located at maxChildIndex
    if (this.storage[index] < this.storage[maxChildIndex]) {
    //swap them      
    [this.storage[maxChildIndex], this.storage[index]] = [this.storage[index], this]
  }
  }
}

module.exports = Heap;
