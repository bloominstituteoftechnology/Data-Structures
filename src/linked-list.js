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
      next: null,
      value: value
     };
     if (!this.head) {
       this.head = node;
       this.tail = node;
     } else {
       this.tail.next = node;
       this.tail = node;
     }
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    if(!this.head) return;
    if (!this.head.next) {
      const value = this.head.value;
      this.head = null;
      this.tail =null;
      return value;
    }
    const value = this.head.value;
    this.head = this.head.next;
    return value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    // iterative solution
    //  if (!this.head) return false;
    // let current = this.head;
    // while (current) {
    //   if (current.value === value) {
    //     return true;
    //   }
    //   current = current.next;
    // }
    // return false;
    const recurse = (node) => {
      if(node.value === value) return true;
      if (!node.next) return false;
      return recurse(node.next);
    };
    return recurse(this.head);
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
      current = current.next
    }
    return max;
  }
}

module.exports = LinkedList;