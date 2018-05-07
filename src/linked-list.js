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

    if (!this.head && !this.tail) {
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
    const removeHead = this.head.value;
    this.head = this.head.next;
    return removeHead;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let found = false;
    let check = this.head;
    while (check) {
      if (check.value === value) {
        found = true;
      }
      check = check.next;
    }
    return found;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let currentValue = this.head;
    let max = null;

    while (currentValue) {
      if (currentValue.value > max) {
        max = currentValue.value;
      }
      currentValue = currentValue.next;
    }
    return max;
  }
}
module.exports = LinkedList;
