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
    const node = { value: value, next: null };
    if (this.head === null) {
      this.head = node;
    } else if (this.tail !== null) {
      this.tail.next = node;
      }
    this.tail = node; 
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    let temp = this.head.value; 
    this.head = this.head.next;
    return temp;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let current = this.head;
    while (current !== null) {
      if (current.value === value) return true;
      current = current.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    // if (this.head === null) return null;
    let highestValue = null;
    let current = this.head;
    while (current !== null) {
      if (current.value > highestValue) highestValue = current.value;
      current = current.next;
    }
    return highestValue;
  }
}

module.exports = LinkedList;