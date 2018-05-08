class Heap {
    /* Do not modify the constructor */
    constructor() {
        this.storage = [];
    }

    /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
    insert(value) {
        const newHeap = new Heap(value);
        if (value > newHeap.storage) {
            // console.log(value, "large");
        }
    }

    /* Remove the maximal value from the heap and
  return it. The heap should maintain the heap
  property after removing the maximal value */
    delete() {}

    /* Return the maximal value in the heap
  without removing it */
    getMax() {
        const maxVal = this.storage[0];
        return maxVal;
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
        // find the index of the parent node
        const parentIndex = Math.floor((index - 1) / 2);
        // check to see if the value at this index needs to be shifted up
        if (this.storage[parentIndex] < this.storage[index]) {
            // if the parent index is less than the new index then shift the new index up
            [this.storage[parentIndex], this.storage[index]] = [this.storage[index], this.storage[parentIndex]];
            // need to repeat process until the new index is in correct position
            // call the function recursively until the new index is in the correct spot
            this.bubbleUp(parentIndex);
        }
    }

    /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
    siftDown(index) {}
}

const newHeap = new Heap(10);
// newHeap.insert(10);

console.log(newHeap);

module.exports = Heap;
