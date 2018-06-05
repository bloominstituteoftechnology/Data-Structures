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
    const node = {
      value: value,
      next: null
    };
    if (this.head === null) this.head = node;
    if (this.tail !== null) this.tail.next = node;
    this.tail = node;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    let node = this.head;
    this.head = node.next;
    return node.value
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let node = this.head;
    while (node !== null) {
      if (node.value === value){
        return true;
      }
        node = node.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let max = 0;
    let node = this.head;
    while (node) {
      if (node.value > max) {
        max = node.value;
      }
      node = node.next;
    }
    return max === 0 ? null : max;
  }
}

module.exports = LinkedList;