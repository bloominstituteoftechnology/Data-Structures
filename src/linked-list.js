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
    // use value to create new node
    const newNode = {
        next: null,
        value,
    };

    // check to see if head is null
    if (this.tail === null) {
        this.head = newNode;
        this.tail = newNode;
        return;
    }
    // change the old tail to point to our new node
    this.tail.next = newNode;
    //update `this.tail` to point to our new node
    this.tail = newNode;
}

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
      const currHead = this.head;
      this.head = this.head.next;
      return currHead.value;
  }
  

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let thisNode = this.head;

    while(thisNode) {
      if(thisNode.value === value) return true;
  
      thisNode = thisNode.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let currNode = this.head;
    let currMax = null;

    if(this.head === null) return null;

    while(currNode){
        if(currNode.value > currMax) {
          currMax = currNode.value
        }
        currNode = currNode.next
      } 
      return currMax; 
  }
}



module.exports = LinkedList;