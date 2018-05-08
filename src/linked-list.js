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
    let secondNode = this.head.next;
    let savedHead = this.head.value;
    
    // if single node, reset to null
    if (this.head === this.tail) {
      this.head = null;
      this.tail = null;
      return savedHead;
    }
    
    // if there are two nodes left, set head to tail
    if (!secondNode.next) {
      this.head = this.tail;
      return savedHead;
    }

    this.head = this.head.next;
    return savedHead;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let currentNode;
    
    // check head
    this.head.value === value
    ? true
    : currentNode = this.head.next;
    
    // traverse list
    while (currentNode.next) {
      currentNode.value === value
      ? true
      : currentNode = currentNode.next;
    }
    
    // check tail
    if (this.tail.value === value) return true;
    
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
   let currentNode = this.head;
   if (!currentNode) return null;
   let max = currentNode.value;
    
   while (currentNode.next) {
    currentNode = currentNode.next;
    if (currentNode.value > max) max = currentNode.value;
   }

   return max;
  }
}

module.exports = LinkedList;
