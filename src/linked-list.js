class LinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
    this.count = 0;
  }

  /* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
  addToTail(value) {
    const node = { value };
    this.length++;
    if (!this.head) {
      this.head = node;
    }
    else {
      this.tail.next = node;
    }
    this.tail = node;

    return value
//<<<<<>>>>>>>
// 
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {

    if (this.head === null) {
      return null;
    }

    const oldHead = this.head;
    this.head = this.head.next || null;
    return oldHead.value;

  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(valued) {
    let thisNode = this.head;

    while (thisNode) {
      if (thisNode.value === valued) {
        return true;
      }
      else {
        thisNode = thisNode.next;
      }

    }

    return false




  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let thisNode = this.head;
    let val = null;
    while (thisNode) {
      if (thisNode.value > val) {
        val = thisNode.value;
      }

      thisNode = thisNode.next;
    }

    return val;

  }
}

module.exports = LinkedList;