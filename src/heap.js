class Heap {
  /* Do not modify the constructor */
  constructor() {
    this.storage = [];
  }

  /* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
  insert(value) {
    const index = this.storage.push(value) -1;
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
    const max = this.storage[0];
    //remove the element with the highest index
    this.storage[0] = this.storage.pop();
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
  bubbleUp(index) { //this is broken! :(
        const arr = this.storage;
        const parentIdx = Math.floor((index - 1) / 2);
    
        if (arr[index] > arr[parentIdx]) {
          [arr[index], arr[parentIdx]] = [arr[parentIdx], arr[index]];
          this.bubbleUp(parentIdx);
        }
      }

  //   const parentIndex = Math.floor((index - 1) /2);
  //   if (this.storage[parentIndex] < this.storage[index]) {
  //     [this.storage[parentIndex], this.storage[index]] = [this.storage[index], ]//is not complete
  //     this.bubbleUp(parentIndex);
  //   }
  // }

  /* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
  siftDown(index) {

        const arr = this.storage;
        const leftIdx = index * 2 + 1;
        const rightIdx = index * 2 + 2;
    
        if (arr[rightIdx] && arr[rightIdx] > arr[index]) {
          [arr[rightIdx], arr[index]] = [arr[index], arr[rightIdx]];
          this.siftDown(rightIdx);
        } else if (arr[leftIdx] && arr[leftIdx] > arr[index]) {
          [arr[leftIdx], arr[index]] = [arr[index], arr[leftIdx]];
          this.siftDown(leftIdx);
        }
      }
  
  //   //grab the two indices that correspond with this index
  //   const leftChildIndex = index * 2 + 1;
  //   const rightChildIndex = index * 2 + 2;
  //   //figure out the larger child
  //   let maxChild;

  //   if(this.storage[leftChildIndex] && this.storage[rightChildIndex]) {
  //     maxChildIndex = this.storage[leftChildIndex] > this.storage[rightChildIndex] ? leftChildIndex : rightChildIndex
  //   } else if (this.storage[leftChildIndex]) {
  //     maxChildIndex = leftChildIndex;
  //   } else if (this.storage[rightChildIndex]) {
  //     maxChildIndex = rightChildIndex;
  //   }

  //   //check to see if we need to swap our current value with the vallue
  //   //located at maxChildIndex
  //   if (this.storage[index] < this.storage[maxChildIndex]) {
  //   //swap them      
  //   [this.storage[maxChildIndex], this.storage[index]] = [this.storage[index], this]
  //     this.siftDown(maxChildIndex);
  // }
  // }
}

module.exports = Heap;
