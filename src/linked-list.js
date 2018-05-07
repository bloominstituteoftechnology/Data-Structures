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
    // check if head is null
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    // change the old tail to point to our new node
    this.tail.next = newNode;
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    if (this.length === 0) {
      return undefined;
    }
    const value = this.head.value;
    this.head = this.head.next;
    this.length--;

    return value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let thisNode = this.head;

    while (thisNode) {
      if (thisNode.value === value) {
        return true;
      }
      thisNode = thisNode.next;
    }

    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if (!this.head) {
      return null;
    }
    let max = 0;
    let head = this.head;

    while (head) {
      if (max < head.value) {
        max = head.value;
      }
      head = head.next;
    }
    return max;
  }
}

module.exports = LinkedList;
