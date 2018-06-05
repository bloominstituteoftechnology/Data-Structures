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
		this.storage.pop();
		if (this.storage.length > 0) {
			let end = this.storage[0];
			this.siftDown(0);
		}
		return end;
	}

	/* Return the maximal value in the heap
  without removing it */
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

	/* Move the element at the specified index "down"
  the heap by swapping it with its larger child if its
  child's value is greater than the value located at
  the input index */
	siftDown(index) {}
}

module.exports = Heap;
