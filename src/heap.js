class Heap {
	/* Do not modify the constructor */
	constructor() {
		this.storage = [];
	}

	/* Insert the given value into the heap.
  The heap should maintain the heap property 
  after insertion */
<<<<<<< HEAD
  insert(value) {
    this.storage.push(value);
    console.log(this.storage);
    this.bubbleUp(this.getSize() - 1);
  }

  /* Remove the maximal value from the heap and
=======
	insert(value) {
		this.storage.push(value);
		this.bubbleUp(this.storage.length - 1);
	}

	/* Remove the maximal value from the heap and
>>>>>>> aa6ee66e82ebc5411c62f86028c1d02adcdf9906
  return it. The heap should maintain the heap
  property after removing the maximal value */
	delete() {
		this.storage.pop();
		if (this.storage.length > 0) {
			let end = this.storage[0];
			this.siftDown(0);
		}
		return end;
	}

	/* Return the maximal value in the heap
  without removing it */
<<<<<<< HEAD
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
    let bubbling = true;
    let temp;
    while (bubbling === true) {
      let parentIndex = Math.floor((index - 1) / 2);
      if (this.storage[index] > this.storage[parentIndex]) {
        temp = this.storage[index];
        this.storage[index] = this.storage[parentIndex];
        this.storage[parentIndex] = temp;
        index = parentIndex;
      } else {
        bubbling = false;
      }
    }
  }
=======
	getMax() {
		let max = 0;
		for (let i = 0; i < this.storage.length; i++) {
			if (this.storage[i] >= this.storage[max]) max = i;
		}
		return this.storage[max];
	}

	/* Return the size of the heap */
	getSize() {
		return this.storage.length;
	}

	/* Moves the element at the specified index "up"
  the heap by swapping it with its parent if its
  parent value is less than the value located at
  the input index */
	bubbleUp(index) {}
>>>>>>> aa6ee66e82ebc5411c62f86028c1d02adcdf9906

	/* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
<<<<<<< HEAD
  siftDown(index) {

  }
=======
	siftDown(index) {}
>>>>>>> aa6ee66e82ebc5411c62f86028c1d02adcdf9906
}

module.exports = Heap;
