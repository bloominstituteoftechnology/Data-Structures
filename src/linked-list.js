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
      return;
    }
    this.tail.next = newNode;
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    if (this.length === 0) {
      return null;
    }

    const value = this.head.value;
    this.head = this.head.next;
    this.length--;

    return value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    if (this.head === value) {
      return true;
    }
    if (this.head !== null) {
      return false;
    }
    return value;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    const currentNode = this.head;
    if (currentNode === null) {
      return 0;
    }
    let max = currentNode + value;
    if (currentNode + value > max) {
      return max;
    }
    return null;
  }
}

module.exports = LinkedList;