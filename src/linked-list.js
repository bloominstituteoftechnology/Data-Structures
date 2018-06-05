class LinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null
    this.tail = null
  }

  /* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
  addToTail(value) {
    const node = {
      value,
      next: null
    }
    if (this.tail) {
      this.tail.next = node
      this.tail = this.tail.next
    } else {
      this.tail = node
      this.head = node
    }
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {}

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {}

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {}
}

module.exports = LinkedList
