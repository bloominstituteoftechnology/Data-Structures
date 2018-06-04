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
    const node = {
      value,
      next: null
    };

    if (this.tail) this.tail.next = node;
    else this.head = node;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    const value = this.head.value;
    this.head = this.head.next;
    return value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let node = this.head;
    while (node) {
      if (node.value === value) return true;
      else node = node.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if(!this.head) return this.head;
    let max = this.head.value;
    let node = this.head.next;
    while (node) {
      if (node.value > max) max = node.value;
      node = node.next;
    }
    return max;
  }
}

module.exports = LinkedList;