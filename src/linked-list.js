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
    // declare newNode with value and next property.
    const newNode = {
      value: value,
      next: null,
    }
    //if no head, create both a head and tail.
    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    //update next pointer for the 'old' tail node to point to the new node and then add new node to the tail. 
    this.tail.next = newNode;
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    //if no head, do not remove anything.
    if (this.head === null) {
      return;
      // if there is a head, remove head by changing both head and tail to null.
    } else if (this.head.next === null) {
      
      const headRemoval = this.head;
      this.head = null;
      this.tail = null;
      return headRemoval.value;
    }
    // return new value of head
    const val = this.head.value;
    this.head = this.head.next;
    return val;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {

  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    
  }
}

module.exports = LinkedList;