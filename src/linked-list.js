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
    if (this.tail) this.tail.next = newNode;
    else this.head = newNode;
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    const head = this.head;
    const nextHead = head.next;
    this.head = nextHead;
    return head.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let currentNode = this.head;
    // loop over the list
    while (currentNode) {
      if (currentNode.value === value) return true;
      currentNode = currentNode.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    
  }
}

module.exports = LinkedList;