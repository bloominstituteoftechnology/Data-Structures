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
      next: null,
    };

    // check to see if head is null
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    // change the old tail to point to our new node
    this.tail.next = newNode;
    // update this.tail to point to our new node
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    if (this.head === null) return null;
    if (!this.head.next) {
      let tmp = this.head;
      this.head = null;
      this.tail = null;
      return tmp.value;
    }
    const tmp = this.head.value;
    this.head = this.head.next;
    return tmp;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let currNode = this.head;
    while (currNode) {
      if (currNode.value === value) return true;
      currNode = currNode.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let head = this.head;
    let max = 0;
    while (head) {
      if (head.value > max) {
        max = head.value;
      }
      head = head.next;
    }
    if (max === 0) {
      return null;
    }
    return max;
  }
}

module.exports = LinkedList;
