class LinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null;
    this.tail = null;
  }
  addToTail(value) {
    const newNode = {
      value,
      next: null
    };
    if (!(this.head) && !(this.tail)) {
      this.head = newNode;
      this.tail = newNode;
    } else {
        this.tail.next = newNode;
        this.tail = newNode;
    }
  // Removes the current head node from the list, replacing it with the next element in the list
  // Returns the value of the removed node
  

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
      const removedHead = this.head.value;
      this.head = this.head.next;
      return removedHead;
    }
    // Checks the linked list for the given value
    // Returns true if the the value is found in the list, false otherwise
    contains(value) {
      let found = false;
      let checkedNode = this.head;
      while (checkedNode) {
        if (checkedNode.value === value) {
          found = true;
        }
        checkedNode = checkedNode.next;
      } return found;
    }
  }
  

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {

  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if(!this.head){
      return null;
    }
    let max=0;
    let myObj=this.head;
    while(myObj){
      if(max<myObj.value) {
        console.log(max);
        max=myObj.value;
        console.log(max);
      }
      console.log(myObj.value);
      myObj=myObj.next;
    }
    return max;
  }
}

module.exports = LinkedList;