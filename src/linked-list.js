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
    if (this.tail === null) {
      // set both head aand tail to the newNode
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
    const removedHead = this.head;

    // change the pointer from the current head, to the next item
    this.head = this.head.next;

    // do a check to make sure, there was only one element, if so, make the tail null too
    if (this.head === null) {
      // also make the tail null
      this.tail = null;
    }

    return removedHead.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    // start search from the head
    for (let node = this.head; node !== null; node = node.next) {
      // check if the values is found and return true
      if (node.value === value) return true; // terminates the for loop
    }
    // to reach here nothing was found
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    // initialize some variable if this.head is not null
    if (this.head === null) return null;
    let node = this.head;
    let max = node.value;

    // this time, I will use a while loop
    while (node !== null) {
      if (max < node.value) max = node.value; //re-assign max value
      // cmove to the next node
      node = node.next;
    }
    return max;
  }
}

// const list = new LinkedList();
// list.addToTail(2);
// list.addToTail(4);
// list.addToTail(3);
// list.addToTail(21);
// list.addToTail(14);
// list.addToTail(33);
// //console.log('+++++', JSON.stringify(list, null, ' '));
// for (let i = list.head; i !== null; i = i.next) {
//   console.log(i);
// }
// console.log('+++++++', list.head);
module.exports = LinkedList;
