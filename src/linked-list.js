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
    const removeHead = this.head.value;
    this.head = this.head.next;
    return removeHead;
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
    let max = null;
    let current = this.head;

    while (current) {
      if (current.value > max) {
        max = current.value;
      }
      current = current.next;
    }
    return max;
  }
}

module.exports = LinkedList;