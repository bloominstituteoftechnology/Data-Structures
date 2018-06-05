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
    this.bubbleUp(this.getSize() - 1);
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    let max = this.storage.shift();
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
    let parentIndex = Math.floor((index - 1) / 2);
    if (this.storage[index] > this.storage[parentIndex]) {
      [this.storage[parentIndex], this.storage[index]] = [this.storage[index], this.storage[parentIndex]];
      this.bubbleUp(parentIndex);
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    let leftChild = (2 * index) + 1;
    let rightChild = (2 * index) + 2;
    let favoriteChild;
    if (this.storage[leftChild] && this.storage[rightChild]) {
      favoriteChild = this.storage[leftChild] > this.storage[rightChild] ? leftChild : rightChild;
    } else if (this.storage[leftChild]) {
      favoriteChild = leftChild;
    } else if (this.storage[rightChild]) {
      favoriteChild = rightChild;
    }

    if (this.storage[favoriteChild] > this.storage[index]) {
      [this.storage[favoriteChild], this.storage[index]] = [this.storage[index], this.storage[favoriteChild]];
      this.siftDown(favoriteChild);
    }
  }
}

module.exports = Heap;
