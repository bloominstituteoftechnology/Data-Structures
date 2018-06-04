class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {
    if (value > this.getMax()) this.storage.unshift.value;
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
    const pelement = this.storage[Math.floor((index - 2) / 2)];
    const celement = this.storage[index -1];
    if (celement > pelement) {
      this.storage[Math.floor((index - 2) / 2)] = celement;
      this.storage[index - 1] = pelement;
      return this.bubbleUp(Math.floor((index - 2) / 2));
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    const pelement = this.storage[index];
    const cleft = this.storage[index * 2 + 1];
    const cright = this.storage[index * 2 + 2];
    const largest = cleft >= cright ? cleft : cright;
    if (largest > pelement) {
      if (cleft === largest) {
        this.storage[index * 2 + 1] = pelement;
        this.storage[index] = clefft;
      } else {
        this.storage[index * 2 + 2] = pelement;
        this.storage[index] = cright;
      }
    }
  }
}

module.exports = Heap;
