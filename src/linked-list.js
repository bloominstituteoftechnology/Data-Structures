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
    value: value, next: null };

    if (!this.head) {
    this.head = newNode;
    this.tail = newNode;
    } else {
    this.tail.next = newNode;
    this.tail = newNode;
    }
  }

  removeHead() {
    const head = this.head;
    this.head = this.head.next;
    return head.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let current = this.head;
    while (current) {
      if (current.value === value) 
      return true;
      current = current.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if (!this.head) return null;

    let current = this.head;
    let max = current.value;
    while (current) {
      if (current.value > max) max = current.value;
      current = current.next;
    }
    return max;
  }
}

module.exports = LinkedList;