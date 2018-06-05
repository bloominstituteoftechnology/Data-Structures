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
    let removed = this.head.value;
    this.head = this.head.next;
    return removed;

  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    // if (this.head.value === value) {
    //   return true;
    // } else if (this.tail.value === value) {
    //   return true;
    // } else {
    //   return false;
    // }
    let current = this.head;
    while (current) {
      if (current.value === value) {
        return true;
      } else {
        current = current.next;
      }
    }
    return false;
    
    // if (this.head.value === value) {
    //   return true;
    // } if (this.head.next === null) {
    //   return false;
    // } if (this.head.next !== null) {
    //   this.head = this.head.next;
    //   return this.contains(value);
    // } 

  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let max = this.tail;
    while (this.head.next != null) {
      this.head = this.head.next;
      if (this.tail.value > max) max = this.tail.value;
    }
    return max;
    
  }
}

module.exports = LinkedList;