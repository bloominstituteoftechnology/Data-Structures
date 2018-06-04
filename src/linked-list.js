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
      value,
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
    let removed = this.head;
    this.head = removed.next;
    return removed.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let current = this.head;
    while (current) {
      if (current.value === value) return true;
      current = current.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let max = null;
    while (this.head !== null) {
      if (max < this.head.value) {
        max = this.head.value;
        this.head = this.head.next;
      }
    }
    return max;
  }
}

module.exports = LinkedList;
