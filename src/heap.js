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
    return this.storage.length;
  }

  /* Moves the element at the specified index "up"
  the heap by swapping it with its parent if its
  parent value is less than the value located at
  the input index */
  bubbleUp(index) {
    const parent = () => Math.floor((index - 1) / 2)
    let p = parent()
    while (index > 0 && this.storage[index] > this.storage[p]) {
      [this.storage[index], this.storage[p]] = [this.storage[p], this.storage[index]]
      index = p, p = parent()
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {
    const left = () => 2 * index + 1
    const right = () => 2 * index + 2
    let l = left(), r = right()
    while (this.storage[l] || this.storage[r]) {
      let swap = this.storage[l] > this.storage[r]
        ? l
        : r
      
      if (this.storage[index] < this.storage[swap]) {
        [this.storage[index], this.storage[swap]] = [this.storage[swap], this.storage[index]]
      } else return
      index = swap, l = left(), r = right()
    }
  }
}

module.exports = Heap;
