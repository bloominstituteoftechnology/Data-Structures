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
    let node = {
      value: value,
      next: null
    }
    if (this.head === null) {
      this.head = node;
      this.head.next = this.tail;
    }
    this.tail = node;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
      if (!this.head) return null;
      let value = this.head;
      this.head = this.head.next;
      
      if (this.head) this.head.prev = null;
      else this.tail = null;
      
      return value;
    }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {

  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {

  }
}

module.exports = LinkedList;