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
      next: null
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
    const removed = this.head;
    this.head = this.head.next;
    removed.next = null;
    return removed.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let found = false;
    let checkedNode = this.head;
    while (checkedNode) {
      if (checkedNode.value === value) {
        found = true;
      }
      checkedNode = checkedNode.next;
    }
    return found;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let maxVal = null;
    while (this.head !== null) {
      if (maxVal < this.head.value) {
        maxVal = this.head.value;
        this.head = this.head.next;
      }
    }
    return maxVal;
  }
}

module.exports = LinkedList;
