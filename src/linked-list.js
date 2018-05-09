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
    if (this.head === null) return;
    if (this.head.next === null) {
      const head = this.head;
      this.head = null;
      this.tail = null;
      return head.value;
    }
    const value = this.head.value;
    this.head = this.head.next;
    return value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    // Recursive solution
    if (this.head === null) return false;
    // const searchLinkedList = (node) => {
    //   // base cases are:
    //   // 1. we find the value
    //   // 2. node.next is null
    //   if (node.value === value) return true;
    //   if (node.next === null) return false;
    //   // call searchLinkedList recursively
    //   // with the next node in the list
    //   return searchLinkedList(node.next);
    // };
    // // call our recursive function on the head node
    // // to kick it off
    // return searchLinkedList(this.head);

    // Iterative solution
    let current = this.head;
    while (current) {
      if (current.value === value) {
        return true;
      }
      current = current.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if (!this.head) return null;
    let max = this.head.value;
    let current = this.head;

    while (current) {
      if (current.value > max) {
        max = current.value;
      }
      current = current.next;
    }

    return max;
  }
}
