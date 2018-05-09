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
      next: null,
    };

    // check if their is a head
    if (this.head === null) {
      // set both head  and tail to the newNode
      this.head = newNode;
      this.tail = newNode;
      return;
    }

    // update the pointer
    this.tail.next = newNode;

    // make the newNode the tail
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    // check if head is null
    if (this.head === null) return null;

    // get copy of the the head
    const head = this.head;

    // check if the next node is null
    if (head.next === null) {
      this.head = null;
      this.tail = null;
    } else {
      // assign the next node as the new head
      this.head = head.next;
    }

    return head.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    // get the start
    let current = this.head;
    if (current === null) return false;
    // start search from the head
    // using the for loop
    // for (let node = current; node !== null; node = node.next) {
    //   // check if the values is found and return true
    //   if (node.value === value) return true; // terminates the for loop
    // }

    // using the while loop
    // while (current) {
    //   if (current.value === value) {
    //     return true;
    //   }
    //   current = current.next;
    // }

    // using the recursive method
    // define a function, and pass in the node
    const searchLinkedList = node => {
      // base cases are:
      // 1. We find the value, return true
      // 2. node.next is null, return false
      if (node.value === value) return true;
      if (node.next === null) return false;

      // call searchLinkedList recursively, passing in the next node
      return searchLinkedList(node.next);
    };

    // initiate the recursive function
    return searchLinkedList(current);

    // to reach here nothing was found
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    // initialize some variable and check if current is not null
    let current = this.head;
    if (!current) return null;

    let max = current.value;
    // this time, I will use a while loop
    while (current) {
      if (current.value > max) max = current.value; //re-assign max value
      // move to the next node
      current = current.next;
    }
    return max;
  }
}

module.exports = LinkedList;
