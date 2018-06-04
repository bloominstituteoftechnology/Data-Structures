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
    // check if tail exists
    if (this.tail) {
      //give previous tail pointer to new tail
      this.tail.next = newNode;
    } else {
      this.head = newNode;
    }
    // set the tail
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    const head = this.head.value;
    this.head = this.head.next;
    return head;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let node = this.head;
    while (node) {
      if (node.value === value) {
        return true;
      } else {
        node = node.next;
      }
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if (!this.head) return null;
    let node = this.head;
    let max = this.head.value;
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
