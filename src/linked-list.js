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
    if(!this.head) {
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
    //remove head and set next node to head?;
    // this.head.value = null;
    // this.head = this.head.next
    // if(this.head.value === null){
    //   return this.head = null
    // }else return this.head.value
    let initHead = this.head.value
    this.head = this.head.next
    return initHead
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let currentNode = this.head;
    while(currentNode !== null) {
      if (currentNode.value === value) {
        return true;
      }
      currentNode = currentNode.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    //if current node is less than next node, swap em
    let currentNode = this.head;
    let currentNodeValue = currentNode.value;
    let max = currentNodeValue;
    for (currentNodeValue)
  }
}

module.exports = LinkedList;