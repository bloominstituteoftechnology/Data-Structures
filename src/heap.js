class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {
    if (value > this.getMax()) {
      this.storage.unshift(value);
    }
    else {
      this.storage.push(value);
      let index = this.getSize() - 1;
      this.bubbleUp(index);
    }

  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    if (!this.storage.length) return null;
    if (this.storage.length === 1) {
      return this.storage.shift();
    };
    const max = this.getMax();
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
    const parentIndex = Math.floor((index - 1) / 2);
    // check to see if the value at this index needs to be shifted up
    if (this.storage[parentIndex] < this.storage[index]) {
      // swap the values at index and parentIndex
      [this.storage[parentIndex], this.storage[index]] = [this.storage[index], this.storage[parentIndex]];
      // recursively call bubbleUp again in case we need to continue shifting
      // the value up the heap
      this.bubbleUp(parentIndex);
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    const leftChidIndex = index * 2 + 1;
    const rightChildIndex = index * 2 + 2;
    let maxChildIndex;
    if (this.storage[leftChidIndex] && this.storage[rightChildIndex]) {
      maxChildIndex = this.storage[leftChidIndex] > this.storage[rightChildIndex] ? leftChidIndex : rightChildIndex;
    }
    else if (this.storage[leftChidIndex]) {
      maxChildIndex = leftChidIndex;
    }
    else if (this.storage[rightChildIndex]) {
      maxChildIndex = rightChildIndex;

    }


    if (this.storage[index] < this.storage[maxChildIndex]) {
      [this.storage[index], this.storage[maxChildIndex]] = [this.storage[maxChildIndex], this.storage[index]]
      this.siftDown(maxChildIndex)
    }

  }

}

module.exports = Heap;


