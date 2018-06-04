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
    newNode = {
      value: value,
      next: null
    };

    if (!this.head) {
      this.head = this.newNode;
      this.tail = this.newNode;
      return;
    }

    this.tail.next = newNode;
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    let currentNode = this.head;
    this.head = currentNode.next
    return currentNode.value
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {}

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {}
}

module.exports = LinkedList;
