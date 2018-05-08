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
    let newNode = { value: value };
    if (this.head) {
      if (!this.tail) {
        this.head.nextNode = newNode;
        this.tail = newNode;
      } else this.tail.nextNode = newNode;
      this.tail = newNode;
    } else {
      this.head = newNode;
      this.tail = newNode;
    }
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    let retObj = this.head;
    // this.head = this.head.nextNode;
    if (this.head.nextNode) this.head = this.head.nextNode;
    else this.head = null;
    return retObj.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    if (this.head.value === value) return true;
    else {
      let curObj = this.head;
      while (1) {
        if (curObj.value === value) return true;
        else if (curObj.nextNode) {
          curObj = curObj.nextNode;
        } else return false;
      }
    }
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let max = 0;
    if (this.head) max = this.head.value;
    else return null;
    let curObj = null;
    if (this.head.nextNode) curObj = this.head.nextNode;
    else return max;
    while (1) {
      if (curObj.value > max) max = curObj.value;
      if (curObj.nextNode) curObj = curObj.nextNode;
      else return max;
    }
  }
}

module.exports = LinkedList;
