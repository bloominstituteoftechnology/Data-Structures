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

    if(!this.head) {
      this.head = newNode;
      this.tail = newNode;
      this.max = value;
      return;
    }

    this.tail.next = newNode;
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    const pugHead = this.head;
    this.head = pugHead.next;
    return pugHead.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let catNode = this.head;

    while(catNode) {
      if(catNode.value === value) return true;
      catNode = catNode.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let max = null;
    let catNode = this.head;
    while(catNode) {
      if(catNode.value > max) max = catNode.value;
      catNode = catNode.next;
    }
    return max;
  }
}

module.exports = LinkedList;