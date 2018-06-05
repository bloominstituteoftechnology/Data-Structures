class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {
    this.storage.push(value)
    this.bubbleUp(this.getSize() - 1)
  }

  /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
  delete() {
    let max = this.storage.shift()
    this.siftDown(0)
    return max
  }

  /* Return the maximal value in the heap
  without removing it */
  getMax() {
    return this.storage[0]
  }

  /* Return the size of the heap */
  getSize() {
    return this.storage.length
  }

  /* Moves the element at the specified index "up"
  the heap by swapping it with its parent if its
  parent value is less than the value located at
  the input index */
  bubbleUp(i) {
    const parentIndex = () => Math.floor((i - 1) / 2)
    let parent = parentIndex()
    while (i > 0 && this.storage[i] > this.storage[parent]) {
      this.swapNodes(i, parent)
      i = parent, parent = parentIndex()
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(i) {
    const leftIndex = () => 2 * i + 1
    const rightIndex = () => 2 * i + 2
    let left = leftIndex(), right = rightIndex()
    while (this.storage[left] || this.storage[right]) {
      let swap = this.storage[left] > this.storage[right]
        ? left
        : right
      
      if (this.storage[i] < this.storage[swap]) {
        this.swapNodes(i, swap)
      } else {
        return
      }
      i = swap, left = leftIndex(), right = rightIndex()
    }
  }

  swapNodes(i, j) {
    const temp = this.storage[i]
    this.storage[i] = this.storage[j]
    this.storage[j] = temp
  }
}

module.exports = Heap;
