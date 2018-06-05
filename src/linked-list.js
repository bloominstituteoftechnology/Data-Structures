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
    };
    if (this.head === null) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    let oldHead = this.head;
    this.head = oldHead.next;
    return oldHead.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let testedNode = this.head;
    while (testedNode === !null) {
      if (testedNode.value === value) {
        return true;
      } else {
        testedNode = testedNode.next;
      }
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {}
}

module.exports = LinkedList;
