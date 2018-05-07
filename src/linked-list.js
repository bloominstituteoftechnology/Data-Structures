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
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    const ans = this.head.value;
    this.head = this.head.next;
    return ans;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let i = this.head;
    while (i) {
      if (i.value === value)
        return true;
      else
        i = i.next;
    }
    return false;

  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if (!this.head)
      return null;
    
    let i = this.head;
    let max = this.head.value;
    while (i) {
      if ( i.value > max)
        max = i.value;
      i = i.next;
    }
    return max;
  }
}

module.exports = LinkedList;