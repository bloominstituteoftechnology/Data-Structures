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
    const index = this.storage.length - 1;
    this.bubbleUp(index);
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    if (!this.storage.length) return null;
    if (this.storage.length === 1) {
      return this.storage.pop();
    }
    // apparently using shift instead of pop is bad
    const biggest = this.storage[0];
    this.storage.shift();
    this.siftDown(0);
    return biggest;
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
    // array destructuring from solution lecture
    if (this.storage[parentIndex] < this.storage[index]) {
      [this.storage[parentIndex], this.storage[index]] = [
        this.storage[index],
        this.storage[parentIndex]
      ];
      this.bubbleUp(parentIndex);
    }
    // my solucione ==================================================
    // const parentIndex = Math.floor((index - 1) / 2);
    // if (this.storage[parentIndex] < this.storage[index]) {
    //   const tempVal = this.storage[parentIndex];
    //   this.storage[parentIndex] = this.storage[index];
    //   this.storage[index] = tempVal;
    // }
    // const grandparentIndex = Math.floor((parentIndex - 1) / 2);
    // if (this.storage[grandparentIndex] < this.storage[parentIndex]) {
    //   this.bubbleUp(parentIndex);
    // }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    const leftChildIndex = index * 2 + 1;
    const rightChildIndex = index * 2 + 2;
    if (this.storage[index] < this.storage[rightChildIndex]) {
      const tempVal = this.storage[rightChildIndex];
      this.storage[rightChildIndex] = this.storage[index];
      this.storage[index] = tempVal;
    } else if (this.storage[index] < this.storage[leftChildIndex]) {
      const tempVal = this.storage[leftChildIndex];
      this.storage[leftChildIndex] = this.storage[index];
      this.storage[index] = tempVal;
    }

    if (index < this.storage.length - 2) {
      this.siftDown(index + 2);
    }
  }
}

module.exports = Heap;
