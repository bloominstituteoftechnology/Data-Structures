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
    const removedMax = this.storage.shift();
    this.siftDown(0);
    return removedMax;
  }

  /* Return the maximal value in the heap
  without removing it */
  getMax() {
    let arr=this.storage;
    let arrMax = Math.max.apply(Math, arr);
    return arrMax
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
    const leftChildIndex = index * 2 + 1;
    const rightChildIndex = index * 2 + 2;
    let greatestChildIndex;
    if (this.storage[leftChildIndex] > this.storage[rightChildIndex])
      greatestChildIndex = leftChildIndex;

    if (this.storage[rightChildIndex] > this.storage[leftChildIndex])
      greatestChildIndex = rightChildIndex;

    if (
      this.storage[index] < this.storage[leftChildIndex] ||
      this.storage[index] < this.storage[rightChildIndex]
    ) {
      [this.storage[index], this.storage[greatestChildIndex]] = [
        this.storage[greatestChildIndex],
        this.storage[index],
      ];
    }
  }
}

module.exports = Heap;
