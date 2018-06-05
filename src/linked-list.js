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
    //should be at the end of the list
    const newNode = {
      value: value,
      next: null
    };
    //check if node isn't null
    if(!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    //changes the previous tail to point towards the new node (i hope)
    this.tail.next = newNode;
    //updates this.tail to point to new node
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    //targets the head of the link
    const linkedHead = this.head.value;
    //changes head to the next head
    this.head = this.head.next;
    return linkedHead;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let linkedNode = this.head;
    while (linkedNode) {
      if (linkedNode.value === value) {
        return true;
      }
      linkedNode = linkedNode.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
  }
}

module.exports = LinkedList;