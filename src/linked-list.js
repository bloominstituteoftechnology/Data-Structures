class LinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null;
    this.tail = null;
  }

  isEmpty() {
    return this.head === null;
  }

  size() {
    let current = this.head;
    let count = 0;
    while (current !== null) {
      count++;
      current = current.next;
    }
    return count;
  }

  addToHead(x) {
    let newNode = {
      value: x,
      next: this.head
    }
    this.head = newNode;
  }

  ///////////////////////////////////////////////////

  /* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
  addToTail(x) {
    const newNode = {
      value: x,
      next: null,
    }
    if (!this.head && !this.tail) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }

    this.tail.next = newNode; /// we  are adding  the newNode to the end of the list by using "next"
    this.tail = newNode; //// we are moving the tail to be the last item in the list which is the newNode 

  }





  /* change  the list's `head` to the next node; 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    // let current = this.head.value;
    // this.head = this.head.next;
    // return current;
    const currentHead = this.head;
    this.head = currentHead.next;
    return currentHead.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(x) {

    let current = this.head;

    while (current !== null) {
      if (current.value === x) {
        return true
      }
      current = current.next; // the current will jump to check the next node ;
    }
    return false;

  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let arr = []
    let current = this.head;
    if (!current) {
      return null;
    }
    while (current !== null) {

      arr.push(current.value)
      current = current.next
    }
    return Math.max(...arr);

  }
}

module.exports = LinkedList;




