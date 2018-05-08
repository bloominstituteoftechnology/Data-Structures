class LinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null;
    this.tail = null;
  }
  //structure is like a nested obj

  /* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
  addToTail(value) {
    const newNode = {
      value: value,
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
  // every node in a linked list has a value and a next property
  removeHead() {
    const removed = this.head;
    this.head = this.head.next;
    return removed.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let found = false;
    let current = this.head;
    // check each node to see if it equals value
    // last node in linked list is always null
    while (current !== null) {
      if (current.value === value) {
        found = true;
        // current = current.next; // breaks the while loop after you found it
        current = null;
      } else {
        current = current.next;
      }
    }
    return found;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  // getMax() {
  //   let max = null;
  //   let current = this.head;
  //   while (current !== null) {
  //     if (current.value > max) {
  //       //compares max to each current value
  //       max = current.value;
  //       current = current.next; // sets current to the next value
  //     } else {
  //       current = current.next; // if current.value < max continue to next node
  //     }
  //   }
  //   return max;
  // }
  getMax() {
    if (!this.head) return null;
    let max = this.head.value;
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
