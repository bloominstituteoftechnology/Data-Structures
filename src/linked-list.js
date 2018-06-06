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
    if (!this.head) { // this creates a new node if none exists at head
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    this.tail.next = newNode; //else if the node exists add a new node to the tail.
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    if(this.head === null) {
      return;
    } else {
      if(this.head.next === null) {
        const head  = this.head;
        this.head = null;
        this.tail = null;
        return head.value;
      }
      const value = this.head.value;
      this.head = this.head.next;
      return value;
    }
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let current = this.head;
    while (current) {
      if (current.value === value) {
        return true;
      } else {
        current = current.next;
      }
      
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if(!this.head) {
      return null;
    } else {
      let max = this.head.value;
      let current = this.head;

      while (current) {
        if(current.value > max) {
          max = current.value;
        } else {
          current = current.next;
        }
      }
      return max;
    }
  }
}

module.exports = LinkedList;