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
    const remove = this.storage.shift();
    this.siftDown(0);
    return remove;
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
    const dex = Math.floor((index - 1) /2);
    if(this.storage[dex] < this.storage[index]) {
      [this.storage[dex], this.storage[index]] = [ this.storage[index], this.storage[dex],];
      this.bubbleUp(dex);
    }

  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
      const l = index * 2 +1;
  const r = index * 2 + 2;
  let lc;
  if(this.storage[l] && this.storage[r]) {
  lc = this.storage[l] > this.storage[r] ? l : r;
  } else if (this.storage[l]) {
    lc = l;
  } else if(this.storage[r]) {
    lc = r;
  }
  if(this.storage[index] < this.storage[lc]) {
    [this.storage[lc], this.storage[index]] = [this.storage[index], this.storage[lc]];
    this.siftDown(lc);
    }
  }
}

module.exports = Heap;
