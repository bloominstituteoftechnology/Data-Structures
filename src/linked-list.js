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
    const tailNode = {
      value,
      next: null
    }
    
    if(this.head === null) {
      this.head = tailNode
      this.tail = tailNode;
    }
    
    this.tail.next = tailNode;
    this.tail = tailNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    const value = this.head.value;
    this.head = this.head.next;
    return value
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let currentNode = this.head;
    while(currentNode) {
      if(currentNode.value === value) return true;
      currentNode = currentNode.next
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    
  }
}

module.exports = LinkedList;