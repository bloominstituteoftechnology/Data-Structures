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
    const node = { value, next: null }

    if (!this.head) { 
      this.head = node 
      this.tail = node
    } else {
      this.tail.next = node;
      this.tail = node;
    }
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    if (!this.head) return null;

    if (!this.head.next) {
      const value = this.head.value;
      this.head = null;
      this.tail = null;
      return value;
    } 
    
    else {
      const value = this.head.value;
      this.head = this.head.next;
      return value;
    }
    // const head = this.head;

    // if (this.head.next === this.tail) {
    //   this.head = this.tail
    //   this.tail = null
    // } else {
    //   this.head = this.head.next
    // }

    // return head.value;

  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    if (!this.head) return false;

    const recurse = node => {
      if (node.value === value) return true;
      if (!node.next) return false;
      return recurse(node.next);
    }

    return recurse(this.head);
    
    // if (!this.head) return false;

    // let current = this.head;

    // while (current) {
    //   if (current.value === value) return true;
    //   current = current.next
    // }

    // return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if (!this.head) return null;

    let max = this.head.value;

    const recurse = node => {
      if (!node) return max;
      if (node.value > max) max = node.value;
      return recurse(node.next);
    }

    return recurse(this.head);
  //   let max = 0;
  //   let current = this.head;

  //   while (current) {
  //     if (current.value > max) max = current.value;
  //     current = current.next;
  //   }
    
  //   return max === 0 ? null : max;
  }
}

module.exports = LinkedList;