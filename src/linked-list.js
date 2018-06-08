// { val: 5
//   next:
//  { val: 6,
//   next: {
//     val: 7,
//     next: {
//       val: 8,
//       next: null
//     }
//   }}}

//   current = this.head


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
    const value = this.head.value;
    this.head = this.head.next;
    if (this.head === null) {
      return this.head = null;
    } else if (this.head.next === null) {
          const value = this.head.value;
          this.head = null;
          this.tail = null;
          return value;
        }
        return value
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let notFound = false;
      if (this.head.value === value) { return true
      check = check.next;
    }
    return notFound;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let node = this.head;
    let max = null;
    while (node) {
      if (node.value > max) {
        max = node.value;
      }
      node = node.next;
    }
    return max;

}

}
module.exports = LinkedList;