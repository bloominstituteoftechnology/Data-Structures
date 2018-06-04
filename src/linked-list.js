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
   }
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
    const remove = this.head;
    this.head = this.head.next;
    return remove.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let current = this.head;
    while (true) {
      if (current.value === value) {
        return true;
      } else if (current.next === null) {
        return false;
      } else {
        current = current.next;
      }
    }
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let currentNode;
    let currentMax;
    if (this.head !== null && this.head !== undefined) {
      currentNode = this.head;
      currentMax = this.head.value;
      while (true) {
        if (currentNode.next !== null) {
          if (currentMax < currentNode.next.value) {
            currentMax = currentNode.next.value;
            currentNode = currentNode.next;
          } else {
            currentNode = currentNode.next;
          }
        } else {
          return currentMax;
        }
      } 
    } else {
      return null;
    }
  }
}

module.exports = LinkedList;