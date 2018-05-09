class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {
    if (this.storage.length === 0) {
      this.storage.push(value);
    } else {
      this.storage.push(value);
      this.bubbleUp(this.storage.length - 1);
    }
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    const removedMax = this.storage.shift();
    this.siftDown(0);
    return removedMax;
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
    if (this.storage[parentIndex] < this.storage[index]) {
      [this.storage[parentIndex], this.storage[index]] = [
        this.storage[index],
        this.storage[parentIndex],
      ];
      this.bubbleUp(parentIndex);
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    const lcd = index * 2 + 1;
    const rcd = index * 2 + 2;
    let gcd;
    if (this.storage[lcd] > this.storage[rcd]) gcd = lcd;

    if (this.storage[rcd] > this.storage[lcd]) gcd = rcd;

    if (
      this.storage[index] < this.storage[lcd] ||
      this.storage[index] < this.storage[rcd]
    ) {
      [this.storage[index], this.storage[gcd]] = [
        this.storage[gcd],
        this.storage[index],
      ];
    }
  }
}

module.exports = Heap;
