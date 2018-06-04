class LinkedList {
	/* Do not modify the constructor */
	constructor() {
		this.head = null;
		this.tail = null;
	}

	/* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
	addToTail(value) {
		const newNode = {
			value: value,
			next: null,
		};
		if (!this.head) {
			this.head = newNode;
			this.tail = newNode;
		} else if (this.head === this.tail) {
			this.head.next = newNode;
			this.tail = newNode;
		} else {
			this.tail.next = newNode;
			this.tail = newNode;
		}
	}

	/* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
	removeHead() {
		const removed = this.head.value;
		this.head = this.head.next;
		return removed;
	}

	/* Searches the list for the given value
  Returns true or false accordingly */
	contains(value) {
		// function checkVal(node, val) {
		// 	if (node.value === val) {
		// 		return true;
		// 	} else {
		// 		checkVal(node.next, val);
		// 	}
		// }
		// checkVal(this.head, value);
		let current = this.head;
		while (current) {
			if (current.value === value) return true;
			else current = current.next
		}
		return false
	}

	/* Finds and returns the maximal value
  of all the values in the list */
	getMax() {
		let result = null;
		let current = this.head;
		while (current) {
			if (current.value > result) result = current.value;
			else current = current.next;
		}
		return result;
	}
}

module.exports = LinkedList;
