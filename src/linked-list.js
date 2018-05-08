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
    // take the value and create a new node from it
    const newNode = {
      value: value,
      next: null
    };
    // check to see if head is null
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    // change the old tail to point to our new node
    this.tail.next = newNode;
    // update `this.tail` to point to our new node.
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    //
    if (this.head === null) return null;
    const removedHead = this.head.value;
    this.head = this.head.next;
    return removedHead;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let found = false;
    let checkedNode = this.head;
    while (checkedNode) {
      if (checkedNode.value === value) {
        found = true;
      }
      checkedNode = checkedNode.next;
    }
    return found;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let maxVal = null;
    while (this.head !== null) {
      if (maxVal < this.head.value) {
        maxVal = this.head.value;
        this.head = this.head.next;
      }
    }
    return maxVal;
  }
}

module.exports = LinkedList;
