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
    const node = { value, next: null }

    if (!this.head) { 
      this.head = node 
      this.tail = node
      return
    }

    this.tail.next = node;
    this.tail = node;
    return
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    const head = this.head;
    if (this.head.next === this.tail) {
      this.head = this.tail
      this.tail = null
    } else {
      this.head = this.head.next
    }
    return head.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let includes = false;
    let current = this.head;

    while (current) {
      if (current.value === value) { includes = true }
      current = current.next
    }

    return includes;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let max = 0;
    let current = this.head;

    while (current) {
      if (current.value > max) max = current.value;
      current = current.next;
    }
    
    return max === 0 ? null : max;
  }
}

module.exports = LinkedList;