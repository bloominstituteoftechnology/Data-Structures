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
  removeHead() {
    if (!this.head) return null;
    let value = this.head.value;
    this.head = this.head.next;
    return value; //this is the value if the head to be deleted
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let thisNode = this.head;
    while (thisNode) {
      if (thisNode.value === value) return true;
      thisNode = thisNode.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let thisNode = this.head;
    let greatest = null;
    while (thisNode) {
      if (greatest < thisNode.value) {greatest = thisNode.value};
      thisNode = thisNode.next;
    }
    return greatest;
  }
}

module.exports = LinkedList;
