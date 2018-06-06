class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

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
    let node = new Node(value);
    let current;
    // update tail to be the new node
    this.tail = node;
    // if list is empty then value is the head
    if (this.head === null) {
      this.head = node;
    } else {
      // list is not empty
      // go to the end and add the value
      current = this.head;

      while (current.next) {
        current = current.next;
      }
      current.next = node;
    }
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    // current head's value that will be removed
    let removed = this.head.value;
    // current head is changed to the next node
    this.head = this.head.next;
    return removed;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let current = this.head;

    // iterate over the list
    // check value against each node's value
    while (current) {
      if (current.value === value) {
        return true;
      } else {
        current = current.next;
      }
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let values = [];
    let current = this.head;

    // collect all values in the list
    while (current) {
      values.push(current.value);

      current = current.next;
    }

    return values.length === 0 ? null : Math.max(...values);
  }
}

module.exports = LinkedList;
