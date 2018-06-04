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
    const parent = () => Math.floor((i - 1) / 2)
    let p = parent()
    while (i > 0 && this.storage[i] > this.storage[p]) {
      [this.storage[i], this.storage[p]] = [this.storage[p], this.storage[i]]
      i = p, p = parent()
    }
  }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(i) {
    const left = () => 2 * i + 1
    const right = () => 2 * i + 2
    let l = left(), r = right()
    while (this.storage[l] || this.storage[r]) {
      let swap = this.storage[l] > this.storage[r]
        ? l
        : r
      
      if (this.storage[i] < this.storage[swap]) {
        [this.storage[i], this.storage[swap]] = [this.storage[swap], this.storage[i]]
      } else return
      i = swap, l = left(), r = right()
    }
  }
}

module.exports = Heap;
